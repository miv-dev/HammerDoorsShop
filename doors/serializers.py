from rest_framework import serializers
from doors.models import Door


class DoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Door
        fields = ['title']
