from django.conf.urls import url
from django.urls import path


from iot import views

urlpatterns = [
    url(r'^switches/$',views.switch_list, name='switch_list'),
    url(r'^switch/(?P<pk>[0-9]+)$', views.switch_detail, name='switch_detail'),
    path('switch/', views.switchbydevice, name='switchbydevice'), #http://127.0.0.1:8000/switch/?device_id=2222&port_number=2
    path('switchdevice/', views.switchfromdevice, name='switchfromdevice'), #http://127.0.0.1:8000/switchdevice/?device_id=1010
    path('test',views.test, name='test')
 
]