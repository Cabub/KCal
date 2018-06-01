from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=512, null=False)

class Portion(models.Model):
    portion = models.CharField(max_length=50, null=False)

class NutritionFact(models.Model):
    name = models.CharField(max_length=50, null=False)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    portion = models.ForeignKey(Portion, on_delete=models.PROTECT)
    count = models.FloatField(null=False)

