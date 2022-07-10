from django.db import models


# Create your models here.
class Profiles(models.Model):
    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
