from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import PersonDetails, CameraDetails,ActivityDetails,ActivityRecord,AnomalyVideoPaths
from .serializers import PersonDetailsSerializer,CameraDetailsSerializer,ActivityDetailsSerializer,ActivityRecordSerializer,AnomalyVideoPathsSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class PersonDetailsAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PersonDetails.objects.all()
    serializer_class = PersonDetailsSerializer

class CameraDetailsAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CameraDetails.objects.all()
    serializer_class = CameraDetailsSerializer

class ActivityDetailsAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ActivityDetails.objects.all()
    serializer_class = ActivityDetailsSerializer

class ActivityRecordAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ActivityRecord.objects.all()
    serializer_class = ActivityRecordSerializer

class AnomalyVideoPathsAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AnomalyVideoPaths.objects.all()
    serializer_class = AnomalyVideoPathsSerializer



