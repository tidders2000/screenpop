
from django.urls import path, include
from meetings.views import meeting_detail, pdf, meeting_requests

urlpatterns = [

    path('meeting_detail', meeting_detail, name='meeting_detail'),
    path('meeting_requests', meeting_requests, name='meeting_requests'),


    path('pdf/<int:pk>/', pdf, name='pdf')

]
