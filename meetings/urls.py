
from django.urls import path, include
from meetings.views import meeting_detail, pdf, meeting_requests, meeting_list, edit_meeting

urlpatterns = [

    path('meeting_detail', meeting_detail, name='meeting_detail'),
    path('meeting_requests', meeting_requests, name='meeting_requests'),
    path('meeting_list', meeting_list, name='meeting_list'),
    path("<int:pk>", edit_meeting, name="edit_meeting"),


    path('pdf/<int:pk>/', pdf, name='pdf')

]
