from . import views
from django.urls import path
from .views import PostList, post_detail

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path("/<slug:slug>/", views.post_detail, name="post_detail"),
]
