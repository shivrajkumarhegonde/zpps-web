from django.db import models

class MidDayMeal(models.Model):
    serial_number = models.IntegerField(verbose_name="अ.क्रं.")
    day = models.CharField(max_length=50, verbose_name="वार")
    food_item = models.CharField(max_length=200, verbose_name="पदार्थ")
    kheer = models.CharField(max_length=200, verbose_name="खीर", blank=True)
    sprouts = models.CharField(max_length=200, verbose_name="स्प्राऊट्स", blank=True)

    def __str__(self):
        return f'{self.day} - {self.food_item}'
