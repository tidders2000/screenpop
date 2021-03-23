
from django.urls import path, include
from .views import blog_add, blog_read

urlpatterns = [
    path('blog_add/', blog_add, name='blog'),
    path('blog_read/', blog_read, name='blogread')
]
