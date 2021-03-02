from iot.serializers import UpdatedDeviceSerializer
from django.conf.urls import url, include
from django.urls import path

from rest_framework import routers

from iot import views

router = routers.DefaultRouter()
router.register(r'updated', views.UpdatedDevice)
# router.register(r'devices', views.FotaUpdateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^switches/$',views.switch_list, name='switch_list'),
    url(r'^switch/(?P<pk>[0-9]+)$', views.switch_detail, name='switch_detail'),
    path('switch/', views.switchbydevice, name='switchbydevice'), #http://127.0.0.1:8000/switch/?device_id=2222&port_number=2
    path('switchdevice/', views.switchfromdevice, name='switchfromdevice'), #http://127.0.0.1:8000/switchdevice/?device_id=1010
    path('test',views.test, name='test'),

    #here urls for the hardware
    path('updates/',views.FotaUpdate.as_view()),
    path('updatedevice/', views.UpdatedDevice),
    
  
    


 
]