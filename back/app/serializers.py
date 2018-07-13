from rest_framework.serializers import ModelSerializer

from .models import Node


class NodeSerializer(ModelSerializer):

    class Meta:
        model = Node
        fields = ['id', 'name']
