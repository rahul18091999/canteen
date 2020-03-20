from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import AdminDetailSerializer
from .models import admindetail

class AdminViewSet(viewsets.ModelViewSet):
    queryset = admindetail.objects.all()
    serializer_class = AdminDetailSerializer
    

