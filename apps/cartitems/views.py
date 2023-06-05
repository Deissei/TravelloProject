from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from apps.cartitems.models import CartItem
from apps.contacts.models import Contact
from apps.gallery.models import Gallery
from apps.homepage.models import SettingMain
from apps.blogs.models import Blog


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

