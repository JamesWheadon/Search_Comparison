from .nodes_edges import Node, Edge

class Graph:
    def __init__(self, map_matrix):
        self.map = map_matrix
        self.nodes = []
        self.edges = []

        self.create_nodes()
        self.create_edges()
    
    def __str__(self):
        return f"Graph with {len(self.nodes)} nodes"
    
    def create_nodes(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] != 0:
                    value = Node(x, y)
                    self.nodes.append(value)
    
    def find_node(self, x, y):
        try:
            return next(node for node in self.nodes if (node.x == x and node.y == y))
        except StopIteration:
            return None
    
    def create_edges(self):
        for node in self.nodes:
            above_node = self.find_node(node.x, node.y - 1)
            if above_node:
                edge = node.connect_to_node(above_node)
                self.edges.append(edge)
            below_node = self.find_node(node.x, node.y + 1)
            if below_node:
                edge = node.connect_to_node(below_node)
                self.edges.append(edge)
            left_node = self.find_node(node.x - 1, node.y)
            if left_node:
                edge = node.connect_to_node(left_node)
                self.edges.append(edge)
            right_node = self.find_node(node.x + 1, node.y)
            if right_node:
                edge = node.connect_to_node(right_node)
                self.edges.append(edge)