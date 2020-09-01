from django.db import models

# Create your models here.
class SpecRamAdd(models.Model):
    Computer = models.CharField(max_length=100, default='')
    Ram = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.Computer

class CityAdd(models.Model):
    City = models.CharField(max_length=100, default='')
    Meters = models.IntegerField(max_length=20, default='')

class Options(models.Model):
    NameHost = models.CharField(max_length=50, default='')
    NameMail = models.CharField(max_length=50, default='')
    PassMail = models.CharField(max_length=50, default='')
    NameToSend = models.CharField(max_length=50, default='')
    NamePort = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.NameMail