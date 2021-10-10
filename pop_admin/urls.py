from django.urls import path, include
from pop_admin.views import pop,editUser

urlpatterns = [

    path('pop', pop, name='pop'),
    path('edituser', editUser, name='edituser')

]
