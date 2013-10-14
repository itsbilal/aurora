from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Community(models.Model):
    owner = models.ForeignKey(User)

    title       = models.CharField(max_length=100)
    slogan      = models.CharField(max_length=140)
    description = models.TextField()

    location    = models.CharField(max_length=50)
    loc_lat     = models.DecimalField(decimal_places=7, blank=True)
    loc_long    = models.DecimalField(decimal_places=7, blank=True)

    term        = models.IntegerField(blank=True) # Blank = unlimited
    cost        = models.DecimalField(blank=True, decimal_places=2) # Blank = Free!


class Membership(models.Model):
    community   = models.ForeignKey(Community)
    member      = models.ForeignKey(User)

    expires     = models.DateField(blank=True)

