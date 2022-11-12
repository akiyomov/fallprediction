from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PersonDetails,CameraDetails, ActivityDetails, ActivityRecord, AnomalyVideoPaths
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = ['id','username','email']
class PersonDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDetails
        fields = '__all__'

class CameraDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraDetails
        fields = '__all__'

class ActivityDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityDetails
        fields = '__all__'

class ActivityRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityRecord
        fields = '__all__'

class AnomalyVideoPathsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnomalyVideoPaths
        fields = '__all__'