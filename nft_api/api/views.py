from django.http import response
import requests
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CollectionSerializer
from .models import collection
from django.shortcuts import get_object_or_404
from web3 import Web3
infura_url = 'https://mainnet.infura.io/v3/1a1c0102684d4fec92f462f9cdcbd63a'
w3 = Web3(Web3.HTTPProvider(infura_url))
print(w3)


# Create your views here.

class CollectionViewset(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = collection.objects.all()

    @action(detail=True)
    def nft(self, request, pk=None):
        Collection = get_object_or_404(collection, pk=pk)
        nft_id = request.GET.get("id")
        url = f"https://api.opensea.io/api/v1/asset/{Collection.address}/{nft_id}/"
        response = requests.get(url).json()
        return Response({"response": response})
