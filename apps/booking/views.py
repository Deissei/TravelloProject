from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView
from django.contrib import messages

from apps.packages.models import Package
from apps.cartitems.models import CartItem

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
        
        return context


def bookingPackage(request):
    carts = CartItem.objects.filter(user=request.user)

    total = 0
    
    for cart_item in carts:
        total+=cart_item.total_price

    # settings main
    setting = SettingMain.objects.get(active=True)
    blogs = Blog.objects.all()[::-1][:2]
    images = Gallery.objects.all()[2:8]
    contacts = Contact.objects.get(id=1)
    return render(request, "booking/booking.html", locals())


def booking_add_package(request, pk):
    if request.method == 'POST':
        print(True)
        form = BookingForm(request.POST)
        cart_item = CartItem.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.cart_item = cart_item
            form.save()
            return redirect('finish_booking', cart_item.id)


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
