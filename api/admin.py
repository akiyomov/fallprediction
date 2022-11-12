from django.contrib import admin
from .models import PersonDetails, CameraDetails,ActivityDetails,ActivityRecord,AnomalyVideoPaths
# Register your models here.
admin.site.register(PersonDetails)
admin.site.register(CameraDetails)
admin.site.register(ActivityDetails)
admin.site.register(ActivityRecord)
admin.site.register(AnomalyVideoPaths)

