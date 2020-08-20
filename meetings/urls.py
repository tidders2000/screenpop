
from django.urls import path, include
from meetings.views import meeting_detail

urlpatterns = [

    path('meeting_detail', meeting_detail, name='meeting_detail'),

]
