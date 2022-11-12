from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import PersonDetails, CameraDetails,ActivityDetails,ActivityRecord,AnomalyVideoPaths
from .serializers import PersonDetailsSerializer,CameraDetailsSerializer,ActivityDetailsSerializer,ActivityRecordSerializer,AnomalyVideoPathsSerializer
# Create your views here.
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



