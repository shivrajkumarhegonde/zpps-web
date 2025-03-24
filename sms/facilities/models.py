from django.db import models
from django.utils import timezone
class Facility(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='facilities/',default='facilities/default.jpg')
    updated_at = models.DateTimeField(auto_now=True)      # Only auto_now

    def __str__(self):
        return self.name