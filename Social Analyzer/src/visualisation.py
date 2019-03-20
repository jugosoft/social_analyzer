import networkx             as nx
import matplotlib.pyplot    as plt

class Graphics:
    G = None

    def __init__(self):
        self.G = nx.DiGraph()

    def add_edge(self, src, dst):
        self.G.add_edges_from([(src, dst)])

    def draw(self):
        val_map = {'A': 1.0,
                   'D': 0.5714285714285714,
                   'H': 0.0}

        values = [val_map.get(node, 0.25) for node in self.G.nodes()]

        # Specify the edges you want here

        edges = [edge for edge in self.G.edges()]

        # Need to create a layout when doing
        # separate calls to draw nodes and edges
        pos = nx.spring_layout(self.G)
        nx.draw_networkx_nodes(self.G, pos, cmap=plt.get_cmap('jet'), 
                               node_color = 'y', node_size = 500)
        nx.draw_networkx_labels(self.G, pos)
        nx.draw_networkx_edges(self.G, pos, edgelist=edges, edge_color='r', arrows=True)

        plt.show()
