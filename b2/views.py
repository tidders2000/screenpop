from django.shortcuts import render


def blog_add(request):
    return render(request, 'blog_add.html')


def blog_read(request):
    return render(request, 'blog_read.html')
