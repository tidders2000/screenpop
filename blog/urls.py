from . import views
from django.urls import path
from .views import PostList, post_detail, add_blog, post_tag

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path("/<slug:slug>/", views.post_detail, name="post_detail"),
    path("add_blog", add_blog, name='add_blog'),

]
