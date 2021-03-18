from django.contrib import admin

from.models import BusinessProfile

# Register your models here.


class BusinessAdmin(admin.ModelAdmin):
    """ Team Role admin view with modifications """
    model = BusinessProfile
    ordering = ('business_name', 'user', )
    list_display = ['business_name', 'user']


admin.site.register(BusinessProfile, BusinessAdmin)
