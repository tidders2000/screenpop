from django.shortcuts import render, redirect, reverse, HttpResponseRedirect,get_object_or_404
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
from business.models import BusinessProfile
from django.contrib.auth.decorators import permission_required

# Create your views here.


@login_required

def group_directory(request):
    groups = Groups.objects.all()
    return render(request, 'groupdirectory.html', {'groups': groups})


@login_required
def group_detail(request, pk):
    group = Groups.objects.get(pk=pk)
    user=request.user
    today = date.today()
    meetings = Meeting.objects.filter(group=group.pk, meeting_date__gte=today)
    members = Switcher.objects.filter(group=group)
    switchData= Switcher.objects.filter(user=user)
    user=switchData[0].business_profile.pk
    print(user)
    return render(request, 'groupdetail.html', {'group': group, 'meetings': meetings, 'members': members,'user':user})


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
    business = BusinessProfile.objects.filter(user=user)
    instance = get_object_or_404(BusinessProfile, pk=business[0].pk)
    print(instance)
    meeting = Meeting.objects.get(pk=pk)
    guest = guests_form().save(commit=False)
    guest.user = user
    guest.meeting = meeting
    guest.business=instance
    guest.save()
    messages.error(request, 'Request added')

    return redirect('group_detail', pk=group)

def edit_group(request):

    groups=add_groups_form()
    qs = Groups.objects.all()
    pk=5

 
    if request.method == "POST":
       name=request.POST.get("group", "")
     
      
       instance=Groups.objects.get(groupName__contains=name)
       
       groups=add_groups_form(instance=instance)
       pk=instance.pk
       return render (request,'edit-group.html',{'qs':qs,'groups':groups,'pk':pk})
     
    
             
          
               
            #         present=group
                   
        
                 
                    # groups = add_groups_form(instance=present)
    return render (request,'edit-group.html',{'qs':qs,'groups':groups,'pk':pk})

def deletegroup(request,pk):
    try:
        b = Groups.objects.get(pk = pk)
        b.delete()
        messages.success(request, "The Group is deleted")            

    except Group.DoesNotExist:
        messages.error(request, "Group doesnot exist")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def changegroupsdetails(request,pk):
        instance = get_object_or_404(Groups, pk=pk)
        if request.method=='POST':
            data = add_groups_form(
            request.POST, request.FILES, instance=instance)
            if data.is_valid():
                data.save(commit=True)
                messages.error(request, "Group Ammended")


        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))