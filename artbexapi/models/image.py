from django.db import models


class Image(models.Model):

    image = models.CharField(max_length=150, blank=True)
    type = models.CharField(max_length=150, blank=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True)
