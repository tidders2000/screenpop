
from django.urls import path, include
from groups.views import group_directory, group_detail

urlpatterns = [
    path('group_directory', group_directory, name='group_directory'),
    path('group_detail', group_detail, name='group_detail'),

]
