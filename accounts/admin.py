from django.contrib import admin


from .models import Profile, Switcher
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )


class SwitcherAdmin(admin.ModelAdmin):
    list_display = ('user', )
    ordering = ('user',)
    search_fields = ['user']
    list_filter =  ['user']


admin.site.register(Profile, ProfileAdmin)

admin.site.register(Switcher, SwitcherAdmin)


# Register your models here.
