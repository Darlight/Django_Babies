from django.contrib import admin
from .models import Baby


class StatusAdmin(admin.ModelAdmin):
	list_attributes = ['name','lastname','parent']
admin.site.register(Baby,StatusAdmin)