from django.db import models


class ArtbexAudience(models.Model):
    artbex = models.ForeignKey(
        "Artbex", on_delete=models.CASCADE, related_name='artbex_audience')
    audience = models.ForeignKey(
        "Audience", on_delete=models.CASCADE, related_name='audience_artbex')

    
