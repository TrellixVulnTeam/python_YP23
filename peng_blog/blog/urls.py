from django.urls import path
from blog.views import *
app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('generic/', generic, name='generic'),
    path('elements/', elements, name='elements'),
    path('<pk>/', detail, name='detail'),
]