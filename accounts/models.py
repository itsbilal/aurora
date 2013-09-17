from django.db import models
from django.contrib.auth.models import User

ACCOUNT_TYPE_CHOICES = (
    ("BS", "Basic"),
    ("PR", "Premium"),
    ("OP", "Organization")
)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    accountType = models.CharField(max_length=2, choices=ACCOUNT_TYPE_CHOICES,
        default="BS")

    expiration = models.DateField(blank=True)
    parent_account = models.ForeignKey(User, blank=True)

class Code(models.Model):
    owner = models.ForeignKey(User)

    code = models.CharField(max_length=10, unique=True)
    used = models.BooleanField(default=False)
    used_by = models.ForeignKey(User, blank=True)
