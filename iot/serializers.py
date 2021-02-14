from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from iot.models import Device, Switch, Weather



class DeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_id','owner', 'created_on')
        read_only_fields = ('device_id',)

class SwitchSerializer(serializers.ModelSerializer):
    # device_id = DeviceSerializers(required=False)
    class Meta:
        model = Switch
        fields = ('id','device_id', 'port_number', 'status','location')

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ('device_id','temperature', 'humidity')