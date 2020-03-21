from .serializer import UserSerializer
from .models import UserDetails
from rest_framework import generics
# Create your views here.

class RegUser(generics.CreateAPIView):
    querset = UserDetails.objects.all()
    serializer_class = UserSerializer
