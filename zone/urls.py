from django.urls import path, include
from zone.views import SlotListAPIView, SlotDetailAPIView

urlpatterns = [
    path('', SlotListAPIView.as_view()),
    path('<int:id>/', SlotDetailAPIView.as_view()),
]
