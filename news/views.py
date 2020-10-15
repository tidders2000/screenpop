from django.shortcuts import render, get_object_or_404
from .models import News
from .forms import add_news_form
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


@login_required
def newsLibrary(request):

    articles = News.objects.all().order_by('date')

    paginator = Paginator(articles, 5)  # Show 5 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "news_library.html", {'page_obj': page_obj})


@ login_required
def newsArticle(request, pk):
    article = get_object_or_404(News, pk=pk)
    return render(request, 'article.html', {'article': article})
