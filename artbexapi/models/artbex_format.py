from django.db import models


class ArtbexFormat(models.Model):
    artbex = models.ForeignKey(
        "Artbex", on_delete=models.CASCADE, related_name='artbex_format')
    format = models.ForeignKey(
        "Format", on_delete=models.CASCADE, related_name='format_artbex')

    
