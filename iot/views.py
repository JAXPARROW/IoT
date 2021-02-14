from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from iot.models import Device, Switch, Weather
from iot.serializers import DeviceSerializers, SwitchSerializer, WeatherSerializer


@csrf_exempt
def switch_list(request):
    #retrieve all objects
    if request.method == 'GET':
        switches = Switch.objects.all()
        switch_serializer = SwitchSerializer(switches, many=True)
        return JsonResponse(switch_serializer.data, safe=False)

@csrf_exempt
def switch_detail(request, pk):
    try:
        switch = Switch.objects.get(pk=pk)
    except Switch.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #retrieve one record
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


class DeviceList(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializers


class SwitchByDevice(generics.ListAPIView):
    serializer_class = SwitchSerializer

    def get_queryset(self):
        queryset = Switch.objects.all()
        device_id = self.request.query_params.get('device_id', None)
        if device_id is not None:
            queryset = queryset.filter(device_id__device_id=device_id)
        return queryset        




