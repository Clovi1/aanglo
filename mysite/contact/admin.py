from django.contrib import admin
from .models import *


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'time_create']
    list_display_links = ['id', 'name', 'email']

    fields = (
        'name', 'email', 'message', 'time_create')
    readonly_fields = ('time_create',)


admin.site.register(About)