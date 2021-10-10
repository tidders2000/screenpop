from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def pop(request):
    return render(request, 'addnews.html')


@login_required
def editUser(request):
    qs = User.objects.all()
    if request.method == "POST":
        print('hello')

    return render (request,'edit-user.html',{'qs':qs})