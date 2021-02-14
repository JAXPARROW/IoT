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
        'location',
        'status'
    ]
    list_display_links = [
        'device_id',
        'location',
        # 'status',
    ]
    list_editable = [
        'status',
    ]
    list_filter = [
        'status',
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


