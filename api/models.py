from tkinter import CASCADE
from django.db import models
from django.utils import timezone as _timezone

class Organizer(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name    

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date_time = models.DateTimeField(default=_timezone.now)
    end_date_time = models.DateTimeField(default=_timezone.now)
    location = models.CharField(max_length=500)
    organizers = models.ManyToManyField(Organizer, blank=True)
    

    def __str__(self):
        return self.title
    
class Ratedate(models.Model):
    date_gte = models.DateField()
    date_lte = models.DateField()