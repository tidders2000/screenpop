from django.contrib import admin

from .models import Meeting, Visitors, Apologies, Guests, Hosts

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Visitors)
admin.site.register(Apologies)
admin.site.register(Guests)
admin.site.register(Hosts)

