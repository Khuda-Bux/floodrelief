from django.db import models

# Create your models here.
class Relief(models.Model):
    name = models.CharField(max_length=100)
    nic = models.IntegerField()
    district = models.CharField(max_length=100)
    tehsil = models.CharField(max_length=100)
    uc = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    photo = models.ImageField()
    date = models.DateTimeField()

