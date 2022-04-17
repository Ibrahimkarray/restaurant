from django.shortcuts import render
from django.http import HttpResponse
from api.models import *
from api.serializers import *
# Create your viewsbyclass here.
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getpersonne(request):
    menus= menu.objects.all()
    serializer=menuserializer(menus,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getpersonnebyid(request,id1):
    menus= menu.objects.get(menu_id=id1)
    serializer=menuserializer(menus,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatepersonne(request,id1):
    data =request.data
    menus=menu.objects.get(menu_id=id1)
    serializer=menuserializer(instance=menus, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletepersonne(request,id1):
    menus=menu.objects.get(menu_id=id1)
    menus.delete()
    return Response('menu was deleted!')

@api_view(['POST'])
def createpersonne(request):

    serializer=menuserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)