from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

class Province(models.Model):
    name = models.CharField(max_length=200)

class City(models.Model):
    name = models.CharField(max_length=200)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
