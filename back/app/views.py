# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Node
from .serializers import NodeSerializer
from.utils.graph.crud.read import find_relatives, node_details
from.utils.graph.crud.write import remove_node


class NodeViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = NodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            search = self.request.GET['search']
            return Node.objects.filter(name__contains=search)
        except:
            return Node.objects.all()


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def delete_node_view(request, node_id):
    remove_node(node_id)
    return Response('node deleted')


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def node_allowed_relatives_view(request):
    """
    Returns the allowed parents or children for the entered node. GET parameters:
    `node`: the node id
    `down`: boolean as 0 or 1; true means that the returned nodes are allowed as children,
                               false means as parents.
    """
    node_id = request.GET['node']
    down = bool(int(request.GET['down']))
    candidates = set(Node.objects.all())
    would_create_loop = set(find_relatives(node_id, not down, 'generalized'))
    are_already_there = set(find_relatives(node_id,     down, 'direct'))
    nodes = candidates.difference(would_create_loop).difference(are_already_there)
    data = json.dumps(
        NodeSerializer(nodes, many=True).data
    )
    return HttpResponse(data, content_type='application/json')


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def node_details_view(request, node_id):
    data = node_details(node_id)
    return HttpResponse(data, content_type='application/json')

