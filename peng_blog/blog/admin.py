# -*- coding:utf-8 -*-
"""常见问题参考官方文档https://docs.djangoproject.com/en/1.10/search/?q=admin"""
from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
"""#  在Django管理中显示文章的标题、内容、时间（要先在models设置）
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    #  编写Django管理中右边的过滤器（记得加逗号）
    list_filter = ('pub_time',)
admin.site.register(Article, ArticleAdmin,)"""
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
