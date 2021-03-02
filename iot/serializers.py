from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from iot.models import Device, Switch, UpdatedDevice, Weather, FotaUpdate

   # "type": "esp8266-fota-http",
    # "version": 1,
    # "host": "192.168.0.105",
    # "port": 80,
    # "bin": "/nodemcu/test.bin"

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_id',)
        read_only_fields = ('device_id',)


class FotaUpdateSerializer(serializers.ModelSerializer):
    device_id = DeviceSerializer()
    class Meta:
        model = FotaUpdate
        fields = ('device_id', 'type', 'version', 'host', 'port', 'bin',)
        


class UpdatedDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdatedDevice
        fields = ('device_id','hardware_id','type', 'version')     


class SwitchSerializer(serializers.ModelSerializer):
    # device_id = DeviceSerializers(required=False)
    device_id = DeviceSerializer(many=False, read_only=True)
    class Meta:
        model = Switch
        fields = ('device_id', 'port_number', 'status','location')

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ('device_id','temperature', 'humidity')