from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Meeting, Visitors, Guests, Apologies
from .forms import meeting_model_form, status_form
from django.contrib import messages
from .utils import render_to_pdf
from django.http import HttpResponse
from accounts.models import Switcher
from django.contrib.auth.decorators import login_required

# Create your views here.


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


@login_required
def pdf(request, pk):

    meeting = Meeting.objects.get(pk=pk)
    grp = meeting.group
    meet = meeting.pk
    attendees = Switcher.objects.filter(group=grp).order_by('user__first_name')
    visitors = Visitors.objects.filter(meeting=meet)
    guests = Guests.objects.filter(meeting=meet)
    apologies = Apologies.objects.filter(meeting=meet)

    data = {'meeting': meeting, 'attendees': attendees,
            'visitors': visitors, 'guests': guests, 'apologies': apologies}

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

    if request.method == "POST":
        meet = meeting_model_form(
            request.POST, request.FILES, instance=instance)
        if meet.is_valid():
            meet.save(commit=True)
            messages.error(request, "Meeting Ammended")

    meeting = meeting_model_form(instance=instance)
    return render(request, 'edit_meeting.html', {'meeting': meeting})
