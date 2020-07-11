from django.db import models

# Create your models here.

class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)