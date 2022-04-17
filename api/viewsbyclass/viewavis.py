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
    aviss= avis.objects.all()
    serializer=avisserializer(aviss,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getpersonnebyid(request,id1):
    aviss= avis.objects.get(avis_id=id1)
    serializer=avisserializer(aviss,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatepersonne(request,id1):
    data =request.data
    aviss=avis.objects.get(avis_id=id1)
    serializer=avisserializer(instance=aviss, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletepersonne(request,id1):
    aviss=avis.objects.get(avis_id=id1)
    aviss.delete()
    return Response('personne was deleted!')

@api_view(['POST'])
def createpersonne(request):

    serializer=avisserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)