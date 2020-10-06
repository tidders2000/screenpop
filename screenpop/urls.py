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
from django.contrib import admin
from django.urls import path, include
from machina import urls as machina_urls
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import index, ServiceWorkerView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('reset', include('password_reset.urls')),
    path('business/', include('business.urls')),
    path('blog/', include('blog.urls')),
    path('chat/', include('chat.urls')),
    path('groups/', include('groups.urls')),
    path('meetings/', include('meetings.urls')),
    path('pop_admin/', include('pop_admin.urls')),
    path('news/', include('news.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('forum/', include(machina_urls)),
    path('', index, name='index'),



    path(
        'sw.js',
        ServiceWorkerView.as_view(),
        name='ServiceWorkerView',
    ),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
