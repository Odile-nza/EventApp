from tkinter import CASCADE
from django.db import models
from django.utils import timezone as _timezone
from django.utils.translation import gettext_lazy as _

class Organizer(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name    

class Event(models.Model):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    DATE_STATUS_CHOICES = (
        (OPEN, _('Open')),
        (CLOSED, _('Closed')),
    )

    title = models.CharField(max_length=200)
    start_date_time = models.DateTimeField(default=_timezone.now)
    end_date_time = models.DateTimeField(default=_timezone.now)
    location = models.CharField(max_length=500)
    organizers = models.ManyToManyField(Organizer, blank=True)
    status = models.CharField(max_length=10, blank=False,choices=DATE_STATUS_CHOICES, default=OPEN)

    def __str__(self):
        return self.title
    
