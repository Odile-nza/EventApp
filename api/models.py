from tkinter import CASCADE
from django.db import models
from django.utils import timezone as _timezone
from django.utils.translation import gettext_lazy as _

class Organizer(models.Model):
    name = models.CharField(max_length=300)
    org_id = models.CharField(max_length=5)
    address = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name    

class Event(models.Model):
    OPEN = 'OPEN'
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=5)
    start_date_time = models.DateTimeField(default=_timezone.now)
    end_date_time = models.DateTimeField(default=_timezone.now)
    location = models.CharField(max_length=500)
    status = models.CharField(max_length=10, blank=False, default=OPEN)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class OrganizersOfEvent(models.Model):
    organizer = models.ForeignKey(Organizer,null=True, blank=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event,null=True, blank=True, on_delete=models.CASCADE)
    
    
# class SafeDelete(Event):
#     isDeleted: models.DateTimeField(null= False, default= False)
#     class Meta:
#      abstract = True