from django.urls import path

from apps.cartitems.views import cart_view


urlpatterns = [
    path('cart/', cart_view, name='cart_view'),
]