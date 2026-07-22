from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# we are creating a table here.
class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title