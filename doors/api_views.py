from rest_framework import viewsets
from .serializers import DoorSerializer
from .models import Door


class DoorViewSet(viewsets.ModelViewSet):
    serializer_class = DoorSerializer
    queryset = Door.objects.all()
