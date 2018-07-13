from app.utils.graph.crud.write import add_node, add_edge

names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen']
for i in range(13):
    add_node(names[i])

edges = [(1, 2), (1, 10), (2, 9), (2, 3), (2, 4), (2, 5), (9, 10), (9, 11), (9, 12), (4, 12), (4, 6), (4, 7), (5, 7), (5, 8), (3, 8), (10, 13), (12, 13)]
for top, bot in edges:
    add_edge(top, bot)
