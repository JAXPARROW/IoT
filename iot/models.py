from django.contrib.admin.options import BaseModelAdmin
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField


SWITCH_STATUS = [
    ("ON" , "ON"),
    ("OFF", "OFF")
]

class Device(models.Model):
    device_id = models.CharField(max_length=10, unique=True, blank=False, null=False)
    owner = CharField(max_length=100, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
   

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    def __str__(self):
        return self.device_id



class Switch(models.Model):
    # device_id = models.CharField(max_length=100, unique=True, blank=False, null=False)
    device_id = models.ForeignKey(Device, related_name='switches', on_delete=models.PROTECT)
    status = models.CharField(max_length=3,choices=SWITCH_STATUS, blank=False, null=False, default="OFF")
    location = models.CharField(max_length=100, blank=False, null=False, default="unknown")


    class Meta:
        verbose_name = 'switch'
        verbose_name_plural = 'switches'

    def __str__(self):
        return self.status

class Weather(models.Model):
    device_id = models.CharField(max_length=100, unique=True, blank=False, null=False)
    temperature = models.FloatField(blank=False, null=False)
    humidity = models.FloatField(blank=False, null=False)

    class Meta:
        verbose_name = 'weather'
        verbose_name_plural = 'weather Devices'

    def __str__(self):
        return int(self.id)
