from nturl2path import url2pathname
from unicodedata import name
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home, name='home'),
    path('map/', views.map, name="map"),
    path('lista/', views.list, name="lista"),
    path(
        'detail_track/<pk>/',
        views.TrackDetailView.as_view(),
        name='detail_track'
    ),
]