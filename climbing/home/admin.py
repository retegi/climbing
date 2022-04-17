from dataclasses import field
from django.contrib import admin
from .models import Track

# Register your models here.

class TrackAdmin(admin.ModelAdmin):
    name = 'name',
    difficulty = 'difficulty'

admin.site.register(Track, TrackAdmin)