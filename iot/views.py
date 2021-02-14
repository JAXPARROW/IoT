from django.db.models import manager
from django.db.models.query_utils import Q
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, request
from django.http.response import JsonResponse
# from django.views.decorators import csrf_exempt

from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser

from iot.models import Device, Switch
from iot.serializers import SwitchSerializer


def test(request):
    if request.method == 'GET':
        switches = Switch.objects.filter(Q(device_id=3333), Q(port_number=1))
        switches_serializer = SwitchSerializer(switches, many=True)
        return JsonResponse(switches_serializer.data, safe=False)

@csrf_exempt
def switchbydevice(request):
    device_id = request.GET.get('device_id','')
    port_number = request.GET.get('port_number','')
    # return HttpResponse(device_id)
    if request.method == 'GET':
        switches = Switch.objects.filter(Q(device_id=device_id), Q(port_number=port_number))
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

    