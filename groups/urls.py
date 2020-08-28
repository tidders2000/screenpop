
from django.urls import path, include
from groups.views import group_directory, group_detail, add_group

urlpatterns = [
    path('group_directory', group_directory, name='group_directory'),
    path('group_detail', group_detail, name='group_detail'),
    path('add_group', add_group, name='add_group'),

]
