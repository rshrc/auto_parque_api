from django.urls import path, include
from entry_log.views import EntryLogListAPIView, EntryLogDetailAPIView

urlpatterns = [
    path('', EntryLogListAPIView.as_view()),
    path('<int:id>/', EntryLogDetailAPIView.as_view()),
]
