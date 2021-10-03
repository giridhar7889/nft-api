from rest_framework import serializers
from .models import collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=collection
        fields=['id','name','address']