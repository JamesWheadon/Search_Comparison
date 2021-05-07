from nodes_edges import Node, Edge

class Graph:
    def __init__(self, map_matrix):
        self.map = map_matrix
        self.nodes = []
        self.edges = []
        self.node_matrix = [[] * len(self.map)]

        self.create_nodes()
    
    def __str__(self):
        return f"Graph with {len(self.nodes)} nodes"
    
    def create_nodes(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                value
                if sel.map[y][x] != 0:
                    value = Node(x, y)
                    self.nodes.append(value)
                else:
                    value = None
                self.node_matrix[y][x] = value