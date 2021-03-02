from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from iot.models import Switch, UpdatedDevice, Weather, Device, FotaUpdate


@admin.register(UpdatedDevice)
class UpdatedDevice(admin.ModelAdmin):
    list_display = ['device_id', 'hardware_id','type','version', 'updated_on']
    list_filter = ['device_id','hardware_id','type','version']
    search_fields = ['device_id','hardware_id','type','version']
    list_per_page = 15


@admin.register(FotaUpdate)
class FotaUpdate(admin.ModelAdmin):
    list_display = ['device_id','type','version','host','bin',]
    list_editable = ['version',]



def switch_off(modeladmin, request, queryset):
    queryset.update(status='OFF')
switch_off.short_description = "Switch OFF the devices"


@admin.register(Device)
class DeviceId(admin.ModelAdmin):
    list_display = ['device_id','owner','created_on',]
    


@admin.register(Switch)
class SwitchAdmin(admin.ModelAdmin):

    #custom admin actions
    def Switch_ON(self, request, queryset):
        update = queryset.update(status='ON')
        self.message_user(request, ngettext(
            '%d devices were switched ON.',
            '%d devices were switched ON.',
            update,
        ) % update, messages.SUCCESS)

    def Switch_OFF(self, request, queryset):
        update = queryset.update(status='OFF')
        self.message_user(request, ngettext(
            '%d devices were switched OFF.',
            '%d devices were switched OFF.',
            update,
        ) % update, messages.SUCCESS)

    actions = [Switch_ON,Switch_OFF,]

    list_display = ['device_id','port_number','location','status']
    list_display_links = ['device_id','location',]
    list_editable = ['status',]
    list_filter = ['status','device_id',]
    search_fields = ['location','device_id','status',]
    
    def switch_On(self, request, queryset):
        update = queryset.update(status='ON')
        self.message_user(request, ngettext(
                '%d devices were switched ON.',
                '%d devices were switched ON.',
                update,
            ) % update, messages.SUCCESS)


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ['device_id','temperature','humidity']


admin.site.site_header = "IoT"
admin.site.site_title = "IoT"