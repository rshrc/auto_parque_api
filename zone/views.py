from rest_framework import generics
from zone.models import Slot, CarSlot
from zone.serializers import SlotSerializer, CarSlotSerializer
from rest_framework.response import Response


class SlotListAPIView(generics.ListCreateAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer


class SlotDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer


class CarSlotIncreaseView(generics.UpdateAPIView):
    queryset = CarSlot.objects.all()
    serializer_class = CarSlotSerializer
    lookup_field = 'id'
   
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.car_count = request.data.get("car_count")

        print("Instance Car Count Type: {}".format(type(instance.car_count)))
        print("Current Car Count: {}".format(instance.car_count))

        instance.car_count = str(int(instance.car_count) + 1)

        print("Updated Car Count: {}".format(instance.car_count))
        serializer = self.get_serializer(data=instance)
        serializer.is_valid(raise_exception=True)

        print(instance)

        instance.save()

        
        # serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class CarSlotDecreaseView(generics.UpdateAPIView):
    pass


class CarSlotCount(generics.RetrieveAPIView):
    pass