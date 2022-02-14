from django.db import models
from django.conf import settings
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1500)
    ratingCount = models.IntegerField(null=True)
    averageRating = models.FloatField(null=True)

class Rating(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()

