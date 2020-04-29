from django.contrib import admin
from .models import Event

class StatusAdmin(admin.ModelAdmin):
	list_display = ['event_type','date','note','baby']
admin.site.register(Event,StatusAdmin)