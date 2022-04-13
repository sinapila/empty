from django.contrib import admin

from . import models


# Register your models here.
from .models import Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'url_title',
        'parent',
        'is_active'
    ]
    list_editable = [
        # 'url_title',
        'parent',
        'is_active'
    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'slug',
        'is_active'
    ]
    list_editable = [
        'is_active'
    ]

    def save_model(self, request, obj: Article, form, change):
        obj.author = request.user
        return super(ArticleAdmin, self).save_model(request,obj,form,change)


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'create_date', 'parent']

admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.ArticleComment, ArticleCommentAdmin)
