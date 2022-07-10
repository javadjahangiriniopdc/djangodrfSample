from django.db import models

# Create your models here.
from myapp.models import Profiles


class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profiles, related_name='posts', on_delete=models.CASCADE)
