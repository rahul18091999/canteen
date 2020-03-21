from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import AdminDetailSerializer
from .models import admindetail
from django.http import JsonResponse

class AdminViewSet(generics.CreateAPIView):
    queryset = admindetail.objects.all()
    serializer_class = AdminDetailSerializer
class AdminDetail(generics.ListAPIView):
    queryset = admindetail.objects.all()
    serializer_class = AdminDetailSerializer

class AdminAuthenticateList(generics.ListAPIView):
    serializer_class = AdminDetailSerializer

    def get_queryset(self):
        msg=admindetail.objects.filter(id=1)
        queryset = admindetail.objects.all()
        email = self.request.query_params.get('email', None)
        password = self.request.query_params.get('password', None)
        if email is not None:
            queryset = queryset.filter(email=email,password=password)
            if queryset:
                print(queryset)
                return queryset
        return msg
    

