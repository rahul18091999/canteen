from rest_framework import serializers
from .models import admindetail

class AdminDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = admindetail
        fields = '__all__'