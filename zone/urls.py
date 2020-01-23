from django.urls import path, include
from zone import views

urlpatterns = [
    path('', views.SlotListAPIView.as_view()),
    path('<int:id>/', views.SlotDetailAPIView.as_view()),
    path('<int:id>/update/', views.CarSlotUpdateView.as_view()),
    path('list/', views.CarSlotListAPIView.as_view()),
]
