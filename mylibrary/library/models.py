from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    publish_year = models.IntegerField()
    colour = models.CharField(max_length=30)
    mileage = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.brand}-{self.publish_year}-{self.colour}-{self.mileage}-{self.price}'