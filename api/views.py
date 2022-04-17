from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
# Create your viewsbyclass here.
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    routes={'ibrahim':'karray'}
    return Response(routes)

