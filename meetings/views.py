from django.shortcuts import render, redirect, reverse
from .models import Meeting, Visitors, Guests, Apologies
from .forms import meeting_model_form, status_form
from django.contrib import messages
from .utils import render_to_pdf
from django.http import HttpResponse
from accounts.models import Switcher

# Create your views here.


def meeting_detail(request):

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
    attendees = Switcher.objects.filter(group=grp)
    visitors = Visitors.objects.filter(meeting=meet)
    guests = Guests.objects.filter(meeting=meet)
    apologies = Apologies.objects.filter(meeting=meet)

    data = {'meeting': meeting, 'attendees': attendees,
            'visitors': visitors, 'guests': guests, 'apologies': apologies}

    pdf = render_to_pdf('pdf/agenda.html', data)

    return HttpResponse(pdf, content_type='application/pdf')


def meeting_requests(request):
    requests = Guests.objects.filter(status='pending')

    if request.method == "POST":

        req = status_form(request.POST)
        nv = req['status'].value()
        pk = request.POST.get('guest_pk')
        user_req = Guests.objects.get(pk=pk)
        user_req.status = nv
        user_req.save()
        return redirect(reverse('dashboard'))
    else:
        form = status_form()

        return render(request, 'meeting_requests.html', {'requests': requests, 'form': form})
