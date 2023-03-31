from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from django.views.generic.base import View


from .models import Package
from apps.homepage.models import SettingMain
from apps.blogs.models import Blog
from apps.gallery.models import Gallery
from apps.contacts.models import Contact

class PackageDetailVew(DetailView):
    model = Package
    slug_field = "slug"
    template_name = "package/package-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        context['images'] = Gallery.objects.all()[2:8]
        context['contacts'] = Contact.objects.get(id=1)
        return context 



class PackageListView(ListView):
    model = Package
    queryset = model.objects.filter(activate_promo=True)
    template_name = "package/package-offer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        context['images'] = Gallery.objects.all()[2:8]
        context['contacts'] = Contact.objects.get(id=1)
        return context 


class PackageNoPromoListView(ListView):
    model = Package
    queryset = model.objects.all()
    template_name = "package/package.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        context['images'] = Gallery.objects.all()[2:8]
        context['contacts'] = Contact.objects.get(id=1)
        return context 
    