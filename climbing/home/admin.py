from dataclasses import field
from django.contrib import admin
from .models import Track, ImageTrack

# Register your models here.

class TrackAdmin(admin.ModelAdmin):
    name = 'name',
    difficulty = 'difficulty'

admin.site.register(Track, TrackAdmin)

class ImageTrackAdmin(admin.ModelAdmin):
    name = 'name',
    track = 'difficulty',
    image_imageTrack = 'image'

admin.site.register(ImageTrack, ImageTrackAdmin)