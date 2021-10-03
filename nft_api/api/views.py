from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CollectionSerializer
from .models import collection


# Create your views here.

class CollectionViewset(viewsets.ModelViewSet):

    serializer_class=CollectionSerializer
    queryset=collection.objects.all()
