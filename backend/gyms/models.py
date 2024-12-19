from django.contrib.auth.models import User
from django.db import models
from backend.basics.models import City, Gender

class Gym(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    postal = models.IntegerField(max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    license_start = models.DateField()
    license_expire = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
