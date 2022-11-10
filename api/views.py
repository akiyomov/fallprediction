from rest_framework.viewsets import ModelViewSet
from .models import Patient
from .serializers import PatientSerializer
# Create your views here.
class PatientAPIView(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
