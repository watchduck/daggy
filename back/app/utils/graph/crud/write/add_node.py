from app.models import Node, Edge


def add_node(node_name):

    node = Node(name=node_name)
    node.save()

    lEdge = Edge(top=node, bot=node, dist=0)
    lEdge.save()

    return node.id
