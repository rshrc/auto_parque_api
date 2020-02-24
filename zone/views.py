from rest_framework import generics
from zone.models import Slot
from zone.serializers import SlotSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
import math
import random

@api_view(['GET'])
def get_slot(request, id):

    try:
        slot = Slot.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SlotSerializer(slot)
        return Response(serializer.data)


@api_view(['GET',])
def get_slot_list(request):

    try:
        slots = Slot.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SlotSerializer(slots, many=True)
        return Response(serializer.data)


@api_view(['PUT',])
def update_slot(request, id):
    print("slot called")
    try:
        slot = Slot.object.get(id=id)
        print(slot)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = SlotSerializer(slot, data=request.data, partial=True)
        data = {}

        if serializer.is_valid():
            serializer.save()
            data['success'] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SlotUpdateView(generics.UpdateAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    lookup_field = 'id'
   
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.car_count = request.data.get("car_count")
        instance.save()  
        return Response(status=status.HTTP_200_OK)



def send_email(request):
    email = EmailMessage(
        'Title',
        f'Email {random.randint(0, 100)}',
        'my-email',
        ['my-receive-email']
    )
    email.send()
