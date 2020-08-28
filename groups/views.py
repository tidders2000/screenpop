from django.shortcuts import render
from .models import Groups
from .forms import add_groups_form
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def group_directory(request):
    groups = Groups.objects.all()
    return render(request, 'groupdirectory.html', {'groups': groups})


@login_required
def group_detail(request):
    return render(request, 'groupdetail.html')


@login_required
def add_group(request):

    if request.method == "POST":
        groups = add_groups_form(request.POST, request.FILES)
        if groups.is_valid():
            groups.save(commit=True)
            messages.error(request, "Group Added")
    else:
        groups = add_groups_form()
    return render(request, 'add_group.html', {'groups': groups})
