# -*- coding:utf-8 -*-
import logging #日志信息
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from.import models
from.models import Post,Category
from django.conf import settings
import markdown
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
logger = logging.getLogger('blog.views')
# Create your views here.

#  导入网站的主体信息
#def global_setting():
    #return {'SITE_NAME':settings.SITE_NAME}

#  定义一个index函数处理http的请求作为一个首页
"""def index(requests):
    try:
        open('sss.txt', 'r')#瞎写的其实没有这个文件，值是为了测试错误日志信息
    except Exception as e:
        logger.error(e)

    post_list = Post.objects.all().order_by('-create_time')
    return render(requests, 'index.html', context={'post_list':post_list})
"""


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})


def detail(request,pk):
    #  当找不到页面时会自动返回404页面
    post=get_object_or_404(Post, pk=pk)
    post.increase_views()
    """这样我们在模板中展示 {{ post.body }} 的时候，就不再是原始的 Markdown 文本了，
    而是渲染过后的 HTML 文本。注意这里我们给 markdown 渲染函数传递了额外的
    参数 extensions，它是对 Markdown 语法的拓展，这里我们使用了三个拓展，
    分别是 extra、codehilite、toc。extra 本身包含很多拓展，而 codehilite 
    是语法高亮拓展，这为我们后面的实现代码高亮功能提供基础，而 toc 则允许我们
    自动生成目录"""
    post.body=markdown.markdown(post.body,extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc',])
    form=CommentForm()
    comment_list=post.comment_set.all()

    context={'post':post, 'form':form, 'comment_list':comment_list}
    return render(request, 'detail.html',context=context)


def generic(request):
    return render(request, 'generic.html', locals())


def elements(request):
    return render(request, 'elements.html', locals())
