from django.db import models
from courses.models import Course

# Create your models here.
# to write this model I got help from chatgpt
class Note(models.Model):
    coursr = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
