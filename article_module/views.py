from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . import models
# Create your views here.
from .models import ArticleCategory, Article, ArticleComment


# Class Base Views

class ArticlesView(ListView):
    template_name = 'article_module/article_page.html'
    model = models.Article
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticlesView, self).get_context_data()
        return context

    def get_queryset(self):
        query = super(ArticlesView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')

        if category_name is not None:
            query = query.filter(selected_category__url_title__iexact=category_name)

        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_detile_page.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(article_id=article.id, parent=None).order_by(
            '-create_date').prefetch_related(
            'articlecomment_set')
        context['comments_count'] = ArticleComment.objects.filter(article_id=article.id, parent=None).count()
        return context


# Function Base Views


def article_categories_partial(request: HttpRequest):
    article_main_categorys = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True, parent_id=None)
    context = {
        'main_categorys': article_main_categorys
    }
    return render(request, 'article_module/partiaals/article_category_partial.html', context)


def AddArticleComment(request: HttpRequest):

    if request.user.is_authenticated:
        article_id = request.GET.get('articleid')
        article_comment = request.GET.get('comment')
        parent_id = request.GET.get('parentid')
        print(article_id, article_comment, parent_id)
        new_commant = ArticleComment(article_id=article_id, text=article_comment, user_id=request.user.id,
                                     parent_id=parent_id)
        new_commant.save()
        return render(request, 'article_module/includes/articlrd_comment_partial.html', {
            'comments': ArticleComment.objects.filter(article_id=article_id, parent=None).order_by(
                '-create_date').prefetch_related('articlecomment_set'),
            'comments_count': ArticleComment.objects.filter(article_id=article_id).count()
        })
    return HttpResponse("hellow")
