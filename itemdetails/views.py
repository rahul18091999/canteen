from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import ItemDetailSerializer
from .models import itemdetail
class ItemViewSet(viewsets.ModelViewSet):
    queryset = itemdetail.objects.all()
    serializer_class = ItemDetailSerializer