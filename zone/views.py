from rest_framework import generics
from zone.models import Slot
from zone.serializers import SlotSerializer


class SlotListAPIView(generics.ListCreateAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer


class SlotDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
