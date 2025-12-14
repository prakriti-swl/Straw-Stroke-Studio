from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Gallery

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

class GalleryView(TemplateView):
    model = Gallery
    template_name = "gallery.html"
    context_object_name = "galleries"

    def get_queryset(self):
        return Gallery.objects.filter(
            published_at__isnull=False
        ).order_by('-published_at')
    

class GalleryDetailView(TemplateView):
    model = Gallery
    template_name = "gallery_detail.html"
    context_object_name = "gallery"

    def get_queryset(self):
        return Gallery.objects.filter(
            published_at__isnull=False
        )
