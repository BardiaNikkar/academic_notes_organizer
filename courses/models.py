from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# we are creating a table here.
class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title