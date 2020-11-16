from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])