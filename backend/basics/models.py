from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " [" + self.gender + "]"


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Building_Ownership(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class License_Ownership(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
