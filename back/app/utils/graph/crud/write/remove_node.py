from app.models import Node, Edge
from .remove_edge import remove_edge


"""
Removing a node requires deleting all edges connected to the node.
When there are ancestors and descendants, it could destroy paths between them or make them longer.
So existing iEdges may have to be deleted or updated with a higher dist.
"""


class NodeNotFoundException(Exception):
    pass


def remove_node(node_id):

    try:
        node = Node.objects.get(id=int(node_id))
    except Node.DoesNotExist:
        raise NodeNotFoundException()

    gA_edges = Edge.objects.filter(bot=node)
    gD_edges = Edge.objects.filter(top=node)

    node_has_rAs_and_rDs = (len(gA_edges) > 1) & (len(gD_edges) > 1)

    if not node_has_rAs_and_rDs:
        gA_edges.delete()
        gD_edges.delete()

    else:

        for e in gA_edges:
            if e.dist == 1:
                remove_edge(e.top.id, e.bot.id)

        for e in gD_edges:
            if e.dist == 1:
                remove_edge(e.top.id, e.bot.id)

    node.delete()
