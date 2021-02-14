from django.conf.urls import url
from django.urls import path
from django.urls.conf import re_path


from iot import views

urlpatterns = [
    # re_path('switch/', views.SwitchList.as_view()), #get all the switches
    path('switches/', views.switch_list, name='switch_list'), #get all the switches
    path('switch_id/<int:pk>/', views.switch_detail),
    re_path('switch/', views.SwitchByDevice.as_view()), #get switch by deviceId
    path('devices/', views.DeviceList.as_view()), #get all the devices
    
 
]