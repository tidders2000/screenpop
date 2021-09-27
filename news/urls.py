
from django.urls import path, include
from .views import addNews, newsLibrary, newsArticle, editNews, deleteNews, delete

urlpatterns = [
    path('add_news/', addNews, name='addNews'),
    path('delete_news/', deleteNews, name='deleteNews'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('edit_news/<int:pk>', editNews, name='editNews'),
    path('news_library/', newsLibrary, name='newsLibrary'),
    path("news_library/<int:pk>/", newsArticle, name="newsArticle"),

]
