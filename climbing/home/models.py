from unittest.util import _MAX_LENGTH
from django.db import models


class Track (models.Model):
    name = models.CharField('Pista', max_length=200, null=True, blank=True)
    difficulty = models.FloatField('Dificultad', null=True, blank=True)
    latitude = models.FloatField('Latitud', null=True, blank=True)
    longitude = models.FloatField('Longitud', null=True, blank=True)
    short_description = models.TextField('Descripción breve', max_length=500, null=True, blank=True)
    full_description = models.TextField('Descripción breve', max_length=500, null=True, blank=True)
    location = models.CharField('Localidad', max_length=100, null=True, blank=True)
    province = models.CharField('Provincia', max_length=100, null=True, blank=True)
    autonomous_community = models.CharField('Comunidad Autonoma', max_length=100, null=True, blank=True)
    country = models.CharField('País', max_length=100, null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "pista"
        verbose_name_plural = "pistas"
    
    def __str__(self):
        return (self.name)
    