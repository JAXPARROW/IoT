from django.conf.urls import url
from django.urls import path


from iot import views

urlpatterns = [
    url(r'^switches/$',views.switch_list, name='switch_list'),
    url(r'^switch/(?P<pk>[0-9]+)$', views.switch_detail, name='switch_detail'),
    path('switch/', views.switchbydevice, name='index'), #http://127.0.0.1:8000/switch/?device_id=2222&port_number=2
    path('test',views.test, name='test')
 
]