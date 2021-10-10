
from django.urls import path, include
from meetings.views import meeting_detail, pdf, meeting_requests, meeting_list, edit_meeting,add_visitor,add_apologies,names

urlpatterns = [

    path('meeting_detail', meeting_detail, name='meeting_detail'),
    path('meeting_requests', meeting_requests, name='meeting_requests'),
    path('meeting_list', meeting_list, name='meeting_list'),
    path('add_visitor', add_visitor, name='add_visitor'),
    path('add_apologies', add_apologies, name='add_apologies'),
    path("<int:pk>", edit_meeting, name="edit_meeting"),
    path("names",names, name="names"),
   


    path('pdf/<int:pk>/', pdf, name='pdf')

]
