from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from app.models import Node, Edge
from . import find_relatives

import json
from app.serializers import NodeSerializer


def node_details(node_id):

    node = Node.objects.get(id=node_id)

    # find relatives

    ancestors   = find_relatives(node_id, False, 'real', Q(dist__in=range(1, 4)))  # 1...3
    descendants = find_relatives(node_id, True,  'real', Q(dist__in=range(1, 7)))  # 1...6

    parents  = find_relatives(node_id, False, 'direct')
    children = find_relatives(node_id, True,  'direct')

    # graph drawing

    edges = []

    # add expected edges above and below node
    for generalized_relatives in [ancestors + [node], descendants + [node]]:
        for n1 in generalized_relatives:
            for n2 in generalized_relatives:
                try:
                    Edge.objects.get(top=n1, bot=n2, dist=1)
                    edges.append((n1.id, n2.id))
                except ObjectDoesNotExist:
                    pass
    # add rather unexpected edges from ancestors to descendants
    for a in ancestors:
        for d in descendants:
            try:
                Edge.objects.get(top=a, bot=d, dist=1)
                edges.append((a.id, d.id))
            except ObjectDoesNotExist:
                pass

    # relnodes = ancestors + [node] + descendants
    # create_graph(node, relnodes, edges)

    relatives_in_both_directions = [
        NodeSerializer(parents, many=True).data,
        NodeSerializer(children, many=True).data
    ]

    return json.dumps(relatives_in_both_directions)
