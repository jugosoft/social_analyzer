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
    def __init__(self):
        """Construstor."""
        self.G = nx.DiGraph()
        self.colour = help.Colour
        self.node_colours = list()
        self.edge_colours = list()

    def add_edge(self, src, dst, colour='y'):
        """
        Adds edge between existing nodes 
        or creates new one. It's not necessary.
        """
        self.G.add_edges_from([(src, dst)])
        self.edge_colours.append(colour)

    def add_node(self, node, colour):
        """
        Adds node
        """
        self.G.add_node(node)
        self.node_colours.append(colour)

    def draw(self):
        self.G.name = 'VKAnalyzer'
        edges = [edge for edge in self.G.edges()]
        # Need to create a layout when doing
        # separate calls to draw nodes and edges
        pos = nx.spring_layout(self.G)
        nx.draw_networkx_nodes(self.G, pos, cmap=plt.get_cmap('jet'), 
                               node_color = self.node_colours, node_size = 25)

        #print(self.node_colours)
        #nx.draw_networkx_labels(self.G, pos)
        nx.draw_networkx_edges(self.G, pos, edgelist=edges, edge_color=self.edge_colours, arrows=False)

        plt.show()
