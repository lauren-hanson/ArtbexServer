from django.db import models


class ArtBex(models.Model):
    images = models.ManyToManyField(
        "Image", through="artbeximage", related_name='images_of_artbex')
    startDate = models.DateField(
        null=True, blank=True, auto_now=False, auto_now_add=False)
    endDate = models.DateField(
        null=True, blank=True, auto_now=False, auto_now_add=False)
    notes = models.CharField(max_length=200)
