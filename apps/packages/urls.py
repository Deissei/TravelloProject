from django.urls import path

from .views import PackageDetailVew, PackageListView, PackageNoPromoListView


urlpatterns = [
    path('packages/', PackageListView.as_view(), name="list_packages"),
    path('packages/<str:slug>', PackageDetailVew.as_view(), name="package_detail"),
    path('tour_package/', PackageNoPromoListView.as_view(), name="no_promo_package"),
]
