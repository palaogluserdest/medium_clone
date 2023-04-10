from django.urls import path
from blog.views import create_blog_post_view

app_name = 'blog'

urlpatterns = [
    #Post Create:
    path('create/', create_blog_post_view, name='create_blog_post_view'),
]
