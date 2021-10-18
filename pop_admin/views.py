from django.http import response
from django.shortcuts import redirect, render,get_object_or_404,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
from accounts.models import Switcher
from business.models import BusinessProfile
from django.contrib import messages
from accounts.forms import user_form,switcher_form


@login_required
def pop(request):
    return render(request, 'addnews.html')


@login_required
def editUser(request):
    userform=user_form()
    qs = User.objects.all()
    term=[]
    pk=1
    switches=[]
    business=[]
    if request.method == "POST":
       name=request.POST.get("user", "")
  
       term =name.split()
   
  
    
    users=User.objects.all()
    if len(term)>0:
        for use in users:
            if use.first_name==term[0] and use.last_name==term[1]:
                    present=use
        
                    switches=Switcher.objects.all().filter(user=present)
                    business=BusinessProfile.objects.all().filter(user=present)
                    userform = user_form(instance=present)
                    pk=present.pk
               

                  
               
            
          


    return render (request,'edit-user.html',{'qs':qs,'switches':switches,'userform':userform,'business':business,'pk':pk})

def changeuserdetails(request,pk):
        instance = get_object_or_404(User, pk=pk)
        if request.method=='POST':
            data = user_form(
            request.POST, request.FILES, instance=instance)
            if data.is_valid():
                data.save(commit=True)
                messages.error(request, "User Ammended")


        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deleteuser(request,pk):
    try:
        u = User.objects.get(pk = pk)
        u.delete()
        messages.success(request, "The user is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")
        

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def editusergroup(request,pk):
     instance = get_object_or_404(Switcher, pk=pk)
     form=switcher_form(instance=instance)
     if request.method=='POST':
            data = switcher_form(
            request.POST, instance=instance)
            if data.is_valid():
                data.save(commit=True)
                messages.error(request, "Group Ammended")
                return redirect(reverse('edituser'))



     return render(request, 'editusergroup.html',{'form':form})

def deleteswitcher(request,pk):
    try:
        s = Switcher.objects.get(pk = pk)
        s.delete()
        messages.success(request, "The Group is deleted")            

    except User.DoesNotExist:
        messages.error(request, "Group doesnot exist")
        

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deletebusiness(request,pk):
    try:
        b = BusinessProfile.objects.get(pk = pk)
        b.delete()
        messages.success(request, "The Business is deleted")            

    except User.DoesNotExist:
        messages.error(request, "Business doesnot exist")
        

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))