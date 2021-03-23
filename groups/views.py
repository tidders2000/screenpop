from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import Groups
from meetings.models import Meeting, Guests
from .forms import add_groups_form
from meetings.forms import guests_form
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from datetime import date
from accounts.models import Switcher

# Create your views here.


@login_required
def group_directory(request):
    groups = Groups.objects.all()
    return render(request, 'groupdirectory.html', {'groups': groups})


@login_required
def group_detail(request, pk):
    group = Groups.objects.get(pk=pk)
    today = date.today()
    meetings = Meeting.objects.filter(group=group.pk, meeting_date__gte=today)
    members = Switcher.objects.filter(group=group)
    return render(request, 'groupdetail.html', {'group': group, 'meetings': meetings, 'members': members})


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


@login_required
def join_meet(request, pk):
    group = request.GET['q']
    user = request.user
    meeting = Meeting.objects.get(pk=pk)
    guest = guests_form().save(commit=False)
    guest.user = user
    guest.meeting = meeting
    guest.save()
    messages.error(request, 'Request added')

    return redirect('group_detail', pk=group)
