# -*- coding:utf-8 -*-
"""在models中设置了新的功能时记得在命令行中输入python manage.py makemigrations
移植数据成功后再在命令行中输入python manage.py migrate进行数据移植"""
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    name = models.CharField('分类名', max_length=100)

    def ___str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    title = models.CharField(max_length=70)
    body = models.TextField()
    #  创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #  文章摘要，可以没有文章摘要，但默认情况下CharField要求我们必须存入数据，否则就会报错
    #  指定CharField的blank=True参数值后就可以允许空值了
    excerpt = models.CharField(max_length=500, blank=True)
    #  我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    #  而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用ManyToManyFiled,表明这是多对多的的关系
    #  同时我们规定文章文章可以没有标签，因此为标签tags指定了blank=True
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE,)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    views=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

