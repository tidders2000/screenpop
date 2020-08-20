from django.shortcuts import render

# Create your views here.


def meeting_detail(request):
    return render(request, 'meeting.html')
