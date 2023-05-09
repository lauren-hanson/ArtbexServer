from django.db import models


class ArtBexImage(models.Model):

    artbex = models.ForeignKey("ArtBex", on_delete=models.CASCADE, blank=True)
    image = models.ForeignKey("Image", on_delete=models.CASCADE, blank=True)
