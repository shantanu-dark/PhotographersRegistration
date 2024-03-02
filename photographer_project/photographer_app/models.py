# photographer_app/models.py
from django.db import models

class Photographer(models.Model):
    business_name = models.CharField(max_length=255)
    camera_equipment = models.TextField()
    lens_used = models.TextField()
    hourly_charges = models.CharField(max_length=50)
    events_covered = models.TextField()
