from rest_framework import serializers
from zone.models import Slot, CarSlot


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ('zone_name', 'index_number', 'empty')


class CarSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSlot
        fields = ('id', 'car_count')