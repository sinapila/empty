from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles_list'),
    path('cat/<str:category>', views.ArticlesView.as_view(), name='articles_by_category_list'),
    path('<pk>/', views.ArticleDetailView.as_view(), name='articles_detail'),
    path('add-article-comment', views.AddArticleComment, name='add_article_comment'),
]
