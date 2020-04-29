from django.contrib import admin
from .models import Parent

class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Parent,StatusAdmin)