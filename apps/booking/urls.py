from django.urls import path
from .views import BookingPackage, BookingAddPackage
from .views import booking_finish


urlpatterns = [
    path("booking/<str:slug>/", BookingPackage.as_view(), name="package_booking"),
    path("add-booking/<int:pk>", BookingAddPackage.as_view(), name="add_booking"),
    path('finish-booking/<int:pk>', booking_finish, name="finish_booking"),
]
