
from django.urls import path, include
from .views import addNews, newsLibrary, newsArticle, editNews

urlpatterns = [
    path('add_news/', addNews, name='addNews'),
    path('edit_news/<int:pk>', editNews, name='editNews'),
    path('news_library/', newsLibrary, name='newsLibrary'),
    path("news_library/<int:pk>/", newsArticle, name="newsArticle"),

]
