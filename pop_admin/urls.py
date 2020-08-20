from django.urls import path, include
from pop_admin.views import pop

urlpatterns = [

    path('pop', pop, name='pop'),

]
