from django.urls import path, include
from pop_admin.views import pop,editUser,changeuserdetails,deleteuser,editusergroup,deleteswitcher,deletebusiness

urlpatterns = [

    path('pop', pop, name='pop'),
    path('edituser', editUser, name='edituser'),
    path('changeuserdetails/<int:pk>/',changeuserdetails,name="changeuserdetails"),
    path('deleteuser/<int:pk>/',deleteuser,name="deleteuser"),
    path('editusergroup/<int:pk>/',editusergroup,name='editusergroup'),
    path('deleteswitcher/<int:pk>/',deleteswitcher,name="deleteswitcher"),
    path('deletebusiness/<int:pk>/',deletebusiness,name="deletebusiness"),

]
