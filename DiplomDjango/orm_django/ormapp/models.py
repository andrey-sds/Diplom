from django.db import models
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    firstname = models.CharField(max_length=30, blank=False)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
