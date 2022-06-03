from django.urls import path
from snacks_api.api.viewset import SnacksListAPIView, SnacksDetailAPIView

urlpatterns = [
    path('api/snacks-list', SnacksListAPIView.as_view(), name='snacks-list'),
    path('api/<int:pk>', SnacksDetailAPIView.as_view(), name='snack-details'),
]