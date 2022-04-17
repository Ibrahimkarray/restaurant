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
    personnes= personne.objects.all()
    serializer=personneserializer(personnes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getpersonnebyid(request,id1):
    personnes= personne.objects.get(pid=id1)
    serializer=personneserializer(personnes,many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updatepersonne(request,id1):
    data =request.data
    personnes=personne.objects.get(pid=id1)
    serializer=personneserializer(instance=personnes, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletepersonne(request,id1):
    personnes=personne.objects.get(pid=id1)
    personnes.delete()
    return Response('personne was deleted!')

@api_view(['POST'])
def createpersonne(request):

    serializer=personneserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

