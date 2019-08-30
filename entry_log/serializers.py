from rest_framework import serializers
from entry_log.models import EntryLog


class EntryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryLog
        fields = ('car_id', 'entry_time')
