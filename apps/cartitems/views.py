from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from apps.cartitems.models import CartItem
from apps.contacts.models import Contact
from apps.gallery.models import Gallery
from apps.homepage.models import SettingMain
from apps.blogs.models import Blog
from apps.packages.models import Package


def cart_view(request):
    # main settings
    setting = SettingMain.objects.get(active=True)

    # blogs 
    blogs = Blog.objects.all()[::-1][:2]

    # footer-contacts
    contacts = Contact.objects.get(id=1)
    images = Gallery.objects.all()[2:8]

    cart_items = CartItem.objects.filter(user=request.user)
    total = 0
    
    for cart_item in cart_items:
        total+=cart_item.total_price 

    return render(request, 'cart/cart.html', locals())

def add_cart(request, pk):
    package = Package.objects.get(id=pk)
    cart = CartItem.objects.create(package=package, user=request.user, quantity=1)
    return redirect('no_promo_package')


def plus_quantity_cart(request, pk):
    cart = CartItem.objects.get(id=pk)
    cart.quantity+=1
    cart.save()
    return redirect('cart_view')


def minus_quantity_cart(request, pk):
    cart = CartItem.objects.get(id=pk)
    cart.quantity-=1
    if cart.quantity > 0:
        cart.save()
    return redirect('cart_view')


def remove_cart_item(request, pk):
    cart = CartItem.objects.get(id=pk)
    cart.delete()
    return redirect('cart_view')