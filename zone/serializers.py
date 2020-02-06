from rest_framework import serializers
from zone.models import Slot, CarSlot

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ('zone_name', 'index_number', 'empty')


# curl -X PUT -d car_count=12 localhost:8000/zone/1/update/
class CarSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSlot
        fields = ('id', 'car_count')


