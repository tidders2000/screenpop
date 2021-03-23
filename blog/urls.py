from . import views
from django.urls import path
from .views import post_list, post_detail, add_blog, post_tag, edit_post

urlpatterns = [
    path('', post_list, name='blog'),
    path("/<slug:slug>/", views.post_detail, name="post_detail"),
    path("add_blog", add_blog, name='add_blog'),
    path("add_blog/<int:pk>", edit_post, name='edit_post'),

]
