from app.models import Node, Edge


"""
Adding a new dEdge could create new paths between gAs and gDs or make them shorter.
So new iEdges may have to be added,
and existing ones may need to be updated with a lower dist.
"""


class AddEdgeException(Exception):

    def __init__(self, message):
        self.message = message


def add_edge(parent_id, child_id):

    parent_id = int(parent_id)
    child_id = int(child_id)

    if parent_id == child_id:
        raise AddEdgeException('parent equals child')

    try:
        parent = Node.objects.get(id=parent_id)
    except Node.DoesNotExist:
        raise AddEdgeException('parent not found')

    try:
        child = Node.objects.get(id=child_id)
    except Node.DoesNotExist:
        raise AddEdgeException('child not found')

    try:
        Edge.objects.get(top=child, bot=parent)
        raise AddEdgeException('child over parent')
    except Edge.DoesNotExist:
        pass

    try:
        rEdge_p_c = Edge.objects.get(top=parent, bot=child)
        if rEdge_p_c.dist == 1:
            raise AddEdgeException('dEdge already exists')
        else:
            rEdge_p_c.dist = 1
            rEdge_p_c.save()
    except Edge.DoesNotExist:
        pass

    gA_edges = Edge.objects.filter(bot=parent)
    gD_edges = Edge.objects.filter(top=child)

    for gA in gA_edges:
        for gD in gD_edges:
            distance = gA.dist + 1 + gD.dist

            try:  # if edge already exists
                rEdge_a_d = Edge.objects.get(top=gA.top, bot=gD.bot)
                if distance < rEdge_a_d.dist:  # if path through parent and child is shorter
                    rEdge_a_d.dist = distance  # write the shorter distance to the DB
                    rEdge_a_d.save()
            except Edge.DoesNotExist:  # if it does not exist
                Edge(top=gA.top, bot=gD.bot, dist=distance).save()  # create it
