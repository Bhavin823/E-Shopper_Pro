from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    GENDER_CHOICE  = (
        ('M','Male'),
        ('F','Female'),
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICE, blank=True)
    
    
