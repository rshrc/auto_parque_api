from rest_framework import serializers
from zone.models import Slot


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ('zone_name', 'index_number', 'empty')
