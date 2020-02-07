from rest_framework import serializers
from zone.models import Slot

# curl -X PUT -d car_count=12 localhost:8000/zone/1/update/
class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ('id', 'car_count')


