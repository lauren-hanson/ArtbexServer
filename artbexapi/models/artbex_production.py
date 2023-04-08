from django.db import models


class ArtbexProduction(models.Model):
    artbex = models.ForeignKey(
        "Artbex", on_delete=models.CASCADE, related_name='artbex_production')
    production = models.ForeignKey(
        "Production", on_delete=models.CASCADE, related_name='production_artbex')

    
