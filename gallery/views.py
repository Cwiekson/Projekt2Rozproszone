from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from gallery.forms import PhotoForm
from gallery.models import Photo


class HomeView(TemplateView):
    template_name = 'home.html'


class PhotoView(CreateView):
    template_name = 'add_photo.html'
    form_class = PhotoForm

    def post(self, request, *args, **kwargs):  # noqa: D102
        form = PhotoForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            photo = form.save()
            photo.save()
            return redirect('succes')
        return redirect('fail')


class GalleryView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.all()
        return context


class SuccesView(TemplateView):
    template_name = 'confirm_add.html'


class FailView(TemplateView):
    template_name = 'fail.html'


