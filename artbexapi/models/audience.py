from django.db import models

class Audience(models.Model):

    type = models.CharField(max_length=150)
    imageUrl = models.CharField(max_length=150, blank=True)