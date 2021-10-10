from django.http.response import JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Meeting, Visitors, Guests, Apologies,Hosts
from .forms import apologies_form, meeting_model_form, status_form,visitors_form
from django.contrib import messages
from .utils import render_to_pdf
from django.http import HttpResponse
from accounts.models import Switcher
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

@login_required
def add_apologies(request):
    form=apologies_form()
    if request.method == "POST":
        apol= apologies_form(request.POST)
        if apol.is_valid():
            apol.save(commit=True)
            messages.error(request, "Apologies Added")

    return render(request,'add_apologies.html',{'form':form})

@login_required
def meeting_detail(request):
    form = meeting_model_form()
    if request.method == "POST":
        meeting = meeting_model_form(request.POST, request.FILES)
        if meeting.is_valid():
            meeting.save(commit=True)
            messages.error(request, "Meeting Added")

    else:
        form = meeting_model_form()
    return render(request, 'add_meeting.html', {'form': form})



def pdf(request, pk):

    meeting = Meeting.objects.get(pk=pk)
    grp = meeting.group
   
    meet = meeting.pk
    host = Hosts.objects.filter(group=grp)
    attendees = Switcher.objects.filter(group=grp).order_by('user__first_name')
    visitors = Visitors.objects.filter(meeting=meet).order_by('first_name')
    guests = Guests.objects.filter(meeting=meet)
    apologies = Apologies.objects.filter(meeting=meet)
    presenter=[]
    if meeting.presenter!=None:
     presenter=meeting.presenter.split()
    
    if len(presenter)>1:

        for attend in attendees:
            if attend.user.first_name==presenter[0] and attend.user.last_name==presenter[1]:
                present=User.objects.get(pk=attend.user.pk)
            
            else:
                present=""
  

    data = {'meeting': meeting, 'attendees': attendees,
            'visitors': visitors, 'guests': guests, 'apologies': apologies, 'host':host,'present':present}

    pdf = render_to_pdf('pdf/agenda.html', data)

    return HttpResponse(pdf, content_type='application/pdf')


@login_required
def meeting_requests(request):
    requests = Guests.objects.filter(status='pending')

    if request.method == "POST":

        req = status_form(request.POST)
        nv = req['status'].value()
        pk = request.POST.get('guest_pk')
        user_req = Guests.objects.get(pk=pk)
        user_req.status = nv
        user_req.save()
        return redirect(reverse('meeting_requests'))
    else:
        form = status_form()

        return render(request, 'meeting_requests.html', {'requests': requests, 'form': form})


@login_required
def meeting_list(request):
    meeting = Meeting.objects.all()

    return render(request, 'meeting_list.html', {'meeting': meeting})


@ login_required
def edit_meeting(request, pk):
    instance = get_object_or_404(Meeting, pk=pk)
    qs = User.objects.all()

    if request.method == "POST":
        meet = meeting_model_form(
            request.POST, request.FILES, instance=instance)
        if meet.is_valid():
            meet.save(commit=True)
            messages.error(request, "Meeting Ammended")

    meeting = meeting_model_form(instance=instance)
    return render(request, 'edit_meeting.html', {'meeting': meeting,'qs':qs})
@ login_required
def add_visitor(request):
     form = visitors_form()
  
     
     if request.method == "POST":
        vis=visitors_form(request.POST)
       
        if vis.is_valid():
            email= vis.cleaned_data.get("email")
            meeting=vis.cleaned_data.get("meeting")
         
            vis.save(commit=True)
            link= 'https://screen-pop.herokuapp.com/meetings/pdf/{}/'.format(meeting.id)
          
            send_mail(subject="ScreenPop App", message="Hi, You have been added as a visitor to attend a ScreenPop networking meeting. Agenda and access link can be found on this link. Meeting link {} Kind regards The ScreenPop Team".format(link),  from_email='admin@screenpop.com',
          
            recipient_list=[email])
            
          
            messages.error(request, "Visitor Added")
           
    
     return render(request, 'add_visitor.html',{'form':form})

def names(request):
     if request.method=="GET":
        
      if 'term' in request.GET:
            qs = User.objects.all()
            return qs