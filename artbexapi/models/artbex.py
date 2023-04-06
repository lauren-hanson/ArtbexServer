from django.db import models


class ArtBex(models.Model):
    tone = models.ForeignKey("Tone", on_delete=models.CASCADE)
    audience = models.ForeignKey("Audience", on_delete=models.CASCADE)
    production = models.ForeignKey("Production", on_delete=models.CASCADE)
    format = models.ForeignKey("Format", on_delete=models.CASCADE)
    startDate = models.DateField(max_length=55)
    endDate = models.DateField(max_length=55)
    notes = models.CharField(max_length=200)
    creator = models.ForeignKey("Creator", on_delete=models.CASCADE)
