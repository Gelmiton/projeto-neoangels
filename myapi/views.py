from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import PrenatalSerializer
from .models import prenatal

class PrenatalViewSet(viewsets.ModelViewSet):
    queryset = prenatal.objects.all().order_by('name')
    serializer_class = PrenatalSerializer
