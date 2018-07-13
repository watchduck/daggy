from django.db.models import Q

from app.models import Edge


def find_relatives(node_id, down, dist, optional_q=Q()):
    """
    Find ancestors or descendants of a node.
    `node_id`
    `down`: true to get descendants
    `dist`: 'direct', 'indirect', 'real' or 'generalized'
    `optional_q`: optional Q object to filter the result
    """

    direction_q = Q(top=node_id) if down else Q(bot=node_id)

    distance_q = {
        'direct':       Q(dist=1),
        'indirect':     Q(dist__gt=1),
        'real':         Q(dist__gt=0),
        'generalized':  Q()
    }[dist]

    edges = Edge.objects.filter(direction_q, distance_q, optional_q)

    found_nodes = []

    for edge in edges:
        node = edge.bot if down else edge.top
        node.dist = edge.dist  # add the dist property directly to the Node object
        found_nodes.append(node)

    return found_nodes
