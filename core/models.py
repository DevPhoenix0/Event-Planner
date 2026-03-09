from django.db import models

# Create your models here.

class Event(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()