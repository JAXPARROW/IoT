from django.contrib import admin

from iot.models import Switch, Weather, Device

@admin.register(Device)
class DeviceId(admin.ModelAdmin):
    list_display = [
        'device_id',
        'owner',
        'created_on',
    ]



@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):
    list_display = [
        'device_id',
        'port_number',
        'location',
        'status'
    ]
    list_display_links = [
        'device_id',
        'location',
    
    ]
    list_editable = [
        'status',
    ]
    list_filter = [
        'status',
        'device_id',
    ]
    search_fields = [
        'location',
        'device_id',
        'status',
    ]



@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = [
        'device_id',
        'temperature',
        'humidity'
    ]


