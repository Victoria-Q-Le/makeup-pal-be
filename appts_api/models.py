from django.db import models

# Create your models here.
class Appt(models.Model):
    name = models.CharField(max_length=32)
    day = models.CharField(max_length=50)
    paid = models.BooleanField()
