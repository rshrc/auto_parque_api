from django.urls import path, include
from zone import views

urlpatterns = [
    path('slot/<int:id>/', views.get_slot),
    path('slot/list/', views.get_slot_list),
    path('slot/update/<int:id>', views.SlotUpdateView.as_view()),
    path('align/fault/', views.send_email),
]
