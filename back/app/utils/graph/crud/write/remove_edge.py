from app.models import Node, Edge
from ..read import find_relatives


"""
Removing a dEdge could destroy paths between gAs and gDs or make them longer.
So existing iEdges may have to be deleted or updated with a higher dist.
"""


class RemoveEdgeException(Exception):

    def __init__(self, message):
        self.message = message


def remove_edge(parent_id, child_id):

    parent_id = int(parent_id)
    child_id = int(child_id)

    if parent_id == child_id:
        raise RemoveEdgeException('parent equals child')

    try:
        parent = Node.objects.get(id=parent_id)
    except Node.DoesNotExist:
        raise RemoveEdgeException('parent not found')

    try:
        child = Node.objects.get(id=child_id)
    except Node.DoesNotExist:
        raise RemoveEdgeException('child not found')

    try:
        dEdge = Edge.objects.get(top=parent, bot=child, dist=1)
        dEdge.delete()
    except Edge.DoesNotExist:
        raise RemoveEdgeException('dEdge not found')

    gAs = set(find_relatives(parent_id, False, 'generalized'))
    gDs = set(find_relatives(child_id,  True,  'generalized'))

    #  t...b  must be kept if there is a path  t...stepparent___stepchild...b
    # with  stepparent...parent  and not  stepchild...parent
    # (... stands for gEdge, ___ for dEdge)

    # For each gA we will need its dDs that are not themselves gAs.
    # (For each ancestor of parent we need its children that are not ancestors of parent.)
    # Such a pair of gA and its dD is a pair of stepparent and stepchild.

    prepared_potential_stepchildren = {}  # returns set of potential stepchildren for stepparent
    for gA in gAs:
        dDs_of_gA = set([e.bot for e in Edge.objects.filter(top=gA, dist=1)])
        prepared_potential_stepchildren[gA] = dDs_of_gA - gAs

    iEdges = Edge.objects.filter(top__in=gAs, bot__in=gDs, dist__gt=1)

    for iEdge in iEdges:
        distances = []  # delete iEdge if empty, otherwise update dist to minimum
        (t, b) = (iEdge.top, iEdge.bot)
        gDs_of_t = set([e.bot for e in Edge.objects.filter(top=t)])
        potential_stepparents = gDs_of_t & gAs
        for sp in potential_stepparents:
            potential_stepchildren = prepared_potential_stepchildren[sp]
            for sc in potential_stepchildren:
                try:
                    gEdge_sc_b = Edge.objects.get(top=sc, bot=b)
                    gEdge_t_sp = Edge.objects.get(top=t, bot=sp)
                    distances.append(gEdge_t_sp.dist + 1 + gEdge_sc_b.dist)
                except:
                    pass
        if distances:
            iEdge.dist = min(distances)
            iEdge.save()
        else:
            iEdge.delete()

