from django.urls import path, include
from zone.views import (
    SlotListAPIView, 
    SlotDetailAPIView,
    CarSlotIncreaseView,
    )

urlpatterns = [
    path('', SlotListAPIView.as_view()),
    path('<int:id>/', SlotDetailAPIView.as_view()),
    path('<int:id>/update/', CarSlotIncreaseView.as_view()),
]
