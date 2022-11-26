from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Image


class IndexView(ListView):
    template_name = 'images.html'
    model = Image
    context_object_name = 'images'
