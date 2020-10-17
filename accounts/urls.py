"""screenpop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import *
from blog.views import post_tag

urlpatterns = [
    path('/', index, name='index'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', registration, name='registration'),
    path('profile/', user_profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('error/', error, name='error'),
    path('reset', include('password_reset.urls')),
    path('switcher/', switcher, name='switcher'),
    path('apologies/<int:pk>', apologies, name='apologies'),
    path('switching/<int:pk>', switching, name='switching'),
    path('switcher_add', switcher_add, name='switcher_add'),
    path('post_tag', post_tag, name='post_tag'),
    path('test', test, name='test'),
    path(
        'sw.js',
        ServiceWorkerView.as_view(),
        name='ServiceWorkerView',
    ),

]
