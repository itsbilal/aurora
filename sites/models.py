from django.db import models
from communities.models import Community

# Create your models here.
class Site(models.Model):
    community = models.OneToOneField(Community)

    title = models.CharField(max_length=140)
