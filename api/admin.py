from django.contrib import admin
from .models import Event, Organizer

class EventAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'start_date_time','end_date_time','location','status',)
    list_filter = ('title',)

admin.site.register(Event, EventAdmin)
admin.site.register(Organizer)

