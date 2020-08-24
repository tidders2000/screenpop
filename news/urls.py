
from django.urls import path, include
from .views import addNews, newsLibrary, newsArticle

urlpatterns = [
    path('add_news/', addNews, name='addNews'),
    path('news_library/', newsLibrary, name='newsLibrary'),
    path("news_library/<int:pk>/", newsArticle, name="newsArticle"),

]
