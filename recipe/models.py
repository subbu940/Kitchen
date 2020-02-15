from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    name = models.CharField(max_length=40)
    ingredients = models.CharField(max_length=200)
    process = models.TextField()
    prep_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

