from rest_framework import generics
from entry_log.models import EntryLog
from entry_log.serializers import EntryLogSerializer


class EntryLogListAPIView(generics.ListCreateAPIView):
    queryset = EntryLog.objects.all()
    serializer_class = EntryLogSerializer


class EntryLogDetailAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = EntryLog.objects.all()
    serializer_class = EntryLogSerializer
