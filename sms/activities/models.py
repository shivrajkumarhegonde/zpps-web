# activities/models.py
from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='activity_images/')

    def __str__(self):
        return f"{self.activity.title} Image"
