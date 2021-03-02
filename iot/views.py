from django.db.models import query
from django.db.models.query_utils import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http.response import JsonResponse


from rest_framework import status, viewsets
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend
import django_filters


from iot.models import Device, Switch, FotaUpdate, UpdatedDevice
from iot.serializers import FotaUpdateSerializer, SwitchSerializer, UpdatedDeviceSerializer


def test(request):
    data = FotaUpdate.objects.all()
    return HttpResponse(data)


class DeviceFilter(django_filters.FilterSet):
    device_id = django_filters.ModelChoiceFilter(field_name="device_id__device_id",
                                            to_field_name = 'device_id',
                                            queryset=Device.objects.all())

    class Meta:
        model = FotaUpdate
        fields = ('device_id',)


class FotaUpdate(generics.ListAPIView):
    queryset = FotaUpdate.objects.all()
    serializer_class = FotaUpdateSerializer
    filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('device_id',)
    filter_class = DeviceFilter


@csrf_exempt
def fotafromdevice(request):
    # device_id = request.GET.get('device_id','')
    # return HttpResponse(device_id)
    if request.method == 'GET':
        queryset = FotaUpdate.objects.all()
        fota_serializer = FotaUpdateSerializer(queryset, many=True)
        return JsonResponse(fota_serializer.data, safe=False)
 

#list of successfully updated devices (CreateRetrieve)
class UpdatedDevice(viewsets.ModelViewSet):
    queryset = UpdatedDevice.objects.all()
    serializer_class = UpdatedDeviceSerializer


#return specific switch from specific device (pass device & port as parameter)
@csrf_exempt
def switchbydevice(request):
    device_id = request.GET.get('device_id','')
    port_number = request.GET.get('port_number','')
    # return HttpResponse(device_id)
    if request.method == 'GET':
        switches = Switch.objects.filter(Q(device_id=device_id), Q(port_number=port_number))
        switches_serializer = SwitchSerializer(switches, many=True)
        return JsonResponse(switches_serializer.data, safe=False)


#return all switches from single device (pass device as parameter)        
@csrf_exempt
def switchfromdevice(request):
    device_id = request.GET.get('device_id','')
    # return HttpResponse(device_id)
    if request.method == 'GET':
        switches = Switch.objects.filter(Q(device_id=device_id))
        switches_serializer = SwitchSerializer(switches, many=True)
        return JsonResponse(switches_serializer.data, safe=False)


@csrf_exempt
def switch_list(request):
    #get all Objects
    if request.method == 'GET':
        switches = Switch.objects.all()
        switches_serializer = SwitchSerializer(switches, many=True)
        return JsonResponse(switches_serializer.data, safe=False)

    #add one object
    if request.method == 'POST':
        switch_data = JSONParser().parse(request)
        switch_serialiazer = SwitchSerializer(data=switch_data)
        if switch_serialiazer.is_valid():
            switch_serialiazer.save()
            return JsonResponse(switch_serialiazer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(switch_serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete object
    if request.method == 'DELETE':
        Switch.objects.all().delete
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def switch_detail(request, pk):
    try:
        switch = Switch.objects.get(pk=pk)
    except Switch.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #retrieve one
    if request.method == 'GET':
        switch_serializer = SwitchSerializer(switch)
        return JsonResponse(switch_serializer.data)

    #update one record
    if request.method == 'PUT':
        switch_data = JSONParser().parse(request)
        switch_serializer = SwitchSerializer(switch, data=switch_data)
        if switch_serializer.is_valid():
            switch_serializer.save()
            return JsonResponse(switch_serializer.data)
        return JsonResponse(switch_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #delete one object
    if request.method == 'DELETE':
        switch.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)



    