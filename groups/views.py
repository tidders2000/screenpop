from django.shortcuts import render

# Create your views here.


def group_directory(request):
    return render(request, 'groupdirectory.html')


def group_detail(request):
    return render(request, 'groupdetail.html')
