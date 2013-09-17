from django.db import models
from django.contrib.auth.models import User

from communities.models import Community

# Create your models here.
class Event(models.Model):
    community   = models.ForeignKey(Community)
    organizer   = models.ForeignKey(User)

    at          = models.DateTimeField()
    ends        = models.DateTimeField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    hours       = models.IntegerField(blank=True) # TODO: Generate this if ends is specified

    attendees   = models.ManyToManyField(User)
    actual_attendees = models.ManyToManyField(User) # If users crack the code, they get to join this elite group.

    code        = models.CharField(max_length=50, blank=True)
