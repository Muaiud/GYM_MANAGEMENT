from rest_framework import serializers
from .models import User,Contact

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','date']
class ContactSerializer(serializers.Serializer):
    class Meta:
        model = Contact
        fields = ['id','name','email','contact','message']        