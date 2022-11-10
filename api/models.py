from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    picture = models.ImageField(blank=True)

    def __str__(self):
        return self.first_name