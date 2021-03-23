
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', profile_upload, name="profile_upload"),
    path('meeting_upload', meeting_upload, name="meeting_upload"),
    path('switcher_upload', switcher_upload, name="switcher_upload"),
    path('business_upload', business_upload, name="business_upload"),
    path('bulk_email', bulk_email, name="bulk_email"),

]
