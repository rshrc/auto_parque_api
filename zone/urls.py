from django.urls import path, include
from zone.views import (
    SlotListAPIView, 
    SlotDetailAPIView,
    CarSlotIncreaseView,
    CarSlotDecreaseView,
    )

urlpatterns = [
    path('', SlotListAPIView.as_view()),
    path('<int:id>/', SlotDetailAPIView.as_view()),
    path('<int:id>/increase/', CarSlotIncreaseView.as_view()),
    path('<int:id>/decrease/', CarSlotDecreaseView.as_view()),
]
