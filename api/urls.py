from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PersonDetailsAPIView,CameraDetailsAPIView,ActivityDetailsAPIView,ActivityRecordAPIView,AnomalyVideoPathsAPIView, MyTokenObtainPairView

router = SimpleRouter()
router.register('person-details',PersonDetailsAPIView,basename='person-details')
router.register('camera-details',CameraDetailsAPIView, basename='camera-details')
router.register('activity-details',ActivityDetailsAPIView,basename='activity-details')
router.register('activity-record',ActivityRecordAPIView,basename='activity-record')
router.register('anomaly-video-paths',AnomalyVideoPathsAPIView,basename='anomaly-video-paths')

urlpatterns = router.urls
urlpatterns += [
    path('login/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
]