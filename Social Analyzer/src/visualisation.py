import networkx             as nx
import matplotlib.pyplot    as plt
import src.helpers          as help

class Graphics:
    """Summary of class goes here.

    This class is a wrapper for 
    comfortable drawing and visual analysis 
    of digraphs.

   Attributes:
       No any attributes yet.
    """
    G = None
    colour = None 

    def __init__(self):
        """Construstor."""
        self.G = nx.DiGraph()
        self.colour = help.Colour

    def add_edge(self, src, dst):
        """
        Adds edge between existing nodes 
        or creates new one. It's not necessary.
        """
        self.G.add_edges_from([(src, dst)])

    def add_node(self, node):
        """
        Adds node
        """
        self.G.add_node(node)

    def draw(self):
        val_map = {'A': 1.0,
                   'D': 0.5714285714285714,
                   'H': 0.0}

        # Specify the edges you want here

        edges = [edge for edge in self.G.edges()]

        # Need to create a layout when doing
        # separate calls to draw nodes and edges
        pos = nx.spring_layout(self.G)
        nx.draw_networkx_nodes(self.G, pos, cmap=plt.get_cmap('jet'), 
                               node_color = self.colour.YELLOW.value, node_size = 15)
        #nx.draw_networkx_labels(self.G, pos)
        nx.draw_networkx_edges(self.G, pos, edgelist=edges, edge_color=self.colour.BLUE.value, arrows=False)

        plt.show()
