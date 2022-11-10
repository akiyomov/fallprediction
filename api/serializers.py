from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = ['id','username','email']
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','first_name','last_name','picture']