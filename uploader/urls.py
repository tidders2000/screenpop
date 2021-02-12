
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', profile_upload, name="profile_upload"),
    path('meeting_upload', meeting_upload, name="meeting_upload"),

]
