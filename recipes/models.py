from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    yield_amount = models.CharField(max_length=255)
    prep_time = models.CharField(max_length=255)
    ingredients = models.TextField()
    directions = models.TextField()
    image = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.title
