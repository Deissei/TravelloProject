from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView
from django.contrib import messages

from apps.packages.models import Package

from .models import Booking

from apps.homepage.models import SettingMain
from apps.blogs.models import Blog
from apps.gallery.models import Gallery
from apps.contacts.models import Contact

from .forms import BookingForm

class BookingPackage(DetailView):
    model = Package
    slug_field = "slug"
    template_name = "booking/booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        context['images'] = Gallery.objects.all()[2:8]
        context['contacts'] = Contact.objects.get(id=1)
        return context
    

class BookingAddPackage(View):
    def post(self, request, pk):
        if request.method == "POST":
            print(True)
            form = BookingForm(request.POST)
            package = Package.objects.get(id=pk)
            if form.is_valid():
                form = form.save(commit=False)
                form.package = package
                form.save()
                return redirect('finish_booking', package.id)
            else:
                messages.info(request, "Не валидное заполнение")
                return redirect('package_booking', package.slug)
        

def booking_finish(request, pk):
    booking = Booking.objects.get(id=pk)
    
    # settings
    setting = SettingMain.objects.get(active=True)
    blogs = Blog.objects.all()[::-1][:2]
    images = Gallery.objects.all()[2:8]
    contacts = Contact.objects.get(id=1)
    return render(request, 'booking/confirmation.html', locals())
