from rest_framework import serializers
from doors.models import Door, Panel, Branch


class PanelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Panel
        fields = ['name', 'image']


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ['name']


class DoorSerializer(serializers.HyperlinkedModelSerializer):
    inside_img = PanelSerializer(many=False)
    branch = BranchSerializer(many=False, read_only=True)
    outside_img = PanelSerializer(many=False)

    class Meta:
        model = Door
        fields = ['title', 'description', 'tech_info', 'branch', 'inside_img', 'outside_img', 'price', 'popular',]


