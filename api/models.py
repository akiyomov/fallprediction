from django.db import models

class PersonDetails(models.Model):
    person_id = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    dob = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    mobile_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_details'
    
    def __str__(self):
        return self.name

class CameraDetails(models.Model):
    camera_id = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camera_details'

    def __str__(self):
        return self.name

class ActivityDetails(models.Model):
    name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_details'
    
    def __str__(self):
        return self.name


class ActivityRecord(models.Model):
    person = models.ForeignKey('PersonDetails', models.DO_NOTHING)
    camera = models.ForeignKey('CameraDetails', models.DO_NOTHING)
    activity = models.ForeignKey(ActivityDetails, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_record'

class AnomalyVideoPaths(models.Model):
    person = models.ForeignKey('PersonDetails', models.DO_NOTHING)
    camera = models.ForeignKey('CameraDetails', models.DO_NOTHING)
    activity = models.ForeignKey(ActivityDetails, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    video_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'anomaly_video_paths'






