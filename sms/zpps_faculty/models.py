from django.db import models

class FacultyMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='faculty_images/', blank=True, null=True)  # Add this field
    bio = models.TextField()

    def __str__(self):
        return self.name
