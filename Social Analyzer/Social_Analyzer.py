import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('Кирилл', 'Алина'),    ('Кирилл', 'Наруто'), 
     ('Наруто', 'Кирилл'),   ('Павел', 'Наруто'), 
     ('Наруто', 'Кристина'), ('Алина', 'Наруто'), 
     ('Наруто', 'Алина')])

val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'H': 0.0}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here

edges = [edge for edge in G.edges()]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                       node_color = 'y', node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', arrows=True)

plt.show()