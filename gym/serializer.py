from rest_framework import serializers
from .models import User

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','date']