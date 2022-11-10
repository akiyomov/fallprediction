from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Patient
from .serializers import PatientSerializer
# Create your views here.
class PatientAPIView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
