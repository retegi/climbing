from unittest.util import _MAX_LENGTH
from django.db import models
from PIL import Image


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

def upload_to(instance, filename): #Esta función genera el directorio al modelo ImageTrack.
    return 'media/img/track/{}/{}'.format(instance.track.id, filename)


class ImageTrack(models.Model):
    name = models.CharField('Título',max_length=100,null=True, blank=True)
    track=models.ForeignKey(Track, related_name="track_image",on_delete=models.CASCADE , null=True, blank=True)
    image_imageTrack = models.ImageField(upload_to=upload_to)

    def save(self, *args, **kwargs):
        instance = super(ImageTrack, self).save(*args, **kwargs)
        image = Image.open(self.image_imageTrack.path)
        image.save(self.image_imageTrack.path, quality=20, optimize=True)
        return instance

    class Meta:
        verbose_name = 'Imagen pista'
        verbose_name_plural = 'Imagen de pistas'
        ordering = ['name']

    def __str__(self):
        return str(self.image_imageTrack)


    