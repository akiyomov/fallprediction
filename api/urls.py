from rest_framework.routers import SimpleRouter
from .views import PatientAPIView

router = SimpleRouter()
router.register('patients',PatientAPIView,basename='patient')

urlpatterns = router.urls