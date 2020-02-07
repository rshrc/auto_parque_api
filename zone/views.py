from rest_framework import generics
from zone.models import Slot
from zone.serializers import SlotSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_slot(request, id):

    try:
        slot = Slot.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SlotSerializer(slot)
        return Response(serializer.data)


@api_view(['GET'])
def get_slot_list(request):

    try:
        slots = Slot.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SlotSerializer(slots, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def update_slot(request, id):

    try:
        slot = Slot.object.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = SlotSerializer(slot, data=request.data)
        data = {}

        if serializer.is_valid():
            serializer.save()
            data['success'] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
