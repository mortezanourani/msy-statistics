from django.contrib.auth.models import User
from django.db import models
from backend.basics.models import City, Gender, Building_Ownership, License_Ownership

class Gym(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    postal = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    building_ownership = models.ForeignKey(Building_Ownership, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    license_start = models.DateField()
    license_expire = models.DateField()
    license_ownership = models.ForeignKey(License_Ownership, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
