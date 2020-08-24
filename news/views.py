from django.shortcuts import render, get_object_or_404
from .models import News
from .forms import add_news_form
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def addNews(request):

    if request.method == "POST":
        news = add_news_form(request.POST, request.FILES)
        if news.is_valid():
            news.save(commit=True)
            messages.error(request, "News Added")
    else:
        news = add_news_form()
    return render(request, 'add_news.html', {'news': news})


def newsLibrary(request):

    articles = News.objects.all()

    return render(request, 'news_library.html', {'articles': articles})


def newsArticle(request, pk):
    article = get_object_or_404(News, pk=pk)
    return render(request, 'article.html', {'article': article})
