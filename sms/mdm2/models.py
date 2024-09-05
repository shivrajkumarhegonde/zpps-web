from django.db import models

class MidDayMeal(models.Model):
    sr_no = models.IntegerField("अ.क्रं.")
    day = models.CharField("वार", max_length=50)
    dish = models.CharField("पदार्थ", max_length=100)  # This should be 'dish'
    kheer = models.CharField("खीर", max_length=100, blank=True, null=True)  # Changed from BooleanField to CharField
    sprouts = models.CharField("स्प्राऊट्स", max_length=100, blank=True, null=True)  # Changed from BooleanField to CharField

    def __str__(self):
        return f"{self.day} - {self.dish}"
