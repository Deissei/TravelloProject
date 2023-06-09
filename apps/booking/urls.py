from django.urls import path
from .views import BookingPackage, BookingAddPackage, bookingPackage, booking_add_package
from .views import booking_finish


urlpatterns = [
    path("booking/<str:slug>/", BookingPackage.as_view(), name="package_booking"),
    path("booking/", bookingPackage, name='booking'),
    path("add-booking/<int:pk>", booking_add_package, name="add_booking"),
    path('finish-booking/<int:pk>', booking_finish, name="finish_booking"),
]
