from django.db import models


class ArtBex(models.Model):
    tone = models.ForeignKey("Tone", on_delete=models.CASCADE)
    startDate = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    endDate = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    notes = models.CharField(max_length=200)
    creator = models.ForeignKey("Creator", on_delete=models.CASCADE)
