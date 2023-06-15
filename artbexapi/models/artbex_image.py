from django.db import models


class ArtBexImage(models.Model):

    artbex = models.ForeignKey("ArtBex", on_delete=models.CASCADE, blank=True, related_name='artbex_image')
    image = models.ForeignKey("Image", on_delete=models.CASCADE, blank=True, related_name='image_artbex')
