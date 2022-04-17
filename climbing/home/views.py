from urllib import request
from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Track, ImageTrack
from django.views.generic.detail import DetailView

def home(request):
    #return HttpResponse('Prueba')
    template = loader.get_template('index.html')
    tracks = Track.objects.all()
    context = { 'tracks' : tracks, }
    #return render(request,'index.html', context)
    return HttpResponse(template.render(context, request))

def map(request):
    #return HttpResponse('Prueba')
    template = loader.get_template('map.html')
    tracks = Track.objects.all()
    context = { 'tracks' : tracks, }
    #return render(request,'index.html', context)
    return HttpResponse(template.render(context, request))

def list(request):
    template = loader.get_template('list_track.html')
    tracks = Track.objects.all()
    context = { 'tracks' : tracks, }
    #return render(request,'index.html', context)
    return HttpResponse(template.render(context, request))


class TrackDetailView(DetailView):
    model = Track
    template_name = "detail_track.html"
    def get_context_data(self, **kwargs):
        name = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['tracks'] = Track.objects.filter(id = name)
        context['images'] = ImageTrack.objects.all()
        return context
