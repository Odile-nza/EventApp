from django.contrib import admin
from .models import Event, Organizer, Ratedate

admin.site.register(Event)
admin.site.register(Organizer)
admin.site.register(Ratedate)

