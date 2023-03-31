from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DestinationList, DestinationDetail

urlpatterns = [
    path('api_destinations_list/', DestinationList.as_view()),
    path('api_destination_detail/<int:pk>', DestinationDetail.as_view()),
]
