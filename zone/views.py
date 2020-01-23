from rest_framework import generics
from zone.models import Slot, CarSlot
from zone.serializers import SlotSerializer, CarSlotSerializer
from rest_framework.response import Response
from rest_framework import status


class SlotListAPIView(generics.ListCreateAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer


class SlotDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer


class CarSlotUpdateView(generics.UpdateAPIView):
    queryset = CarSlot.objects.all()
    serializer_class = CarSlotSerializer
    lookup_field = 'id'
   
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.car_count = request.data.get("car_count")
        instance.save()  
        return Response(status=status.HTTP_200_OK)


class CarSlotListAPIView(generics.ListAPIView):
    queryset = CarSlot.objects.all()
    serializer_class = CarSlotSerializer


class CarSlotDecreaseView(generics.UpdateAPIView):
    pass


class CarSlotCount(generics.RetrieveAPIView):
    pass