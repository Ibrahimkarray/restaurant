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
    userss= users.objects.all()
    serializer=usersserializer(userss,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getpersonnebyid(request,id1):
    userss= users.objects.get(uid=id1)
    serializer=usersserializer(userss,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatepersonne(request,id1):
    data =request.data
    userss=users.objects.get(uid=id1)
    serializer=usersserializer(instance=userss, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletepersonne(request,id1):
    userss=users.objects.get(uid=id1)
    users.delete()
    return Response('user was deleted!')

@api_view(['POST'])
def createpersonne(request):

    serializer=usersserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)