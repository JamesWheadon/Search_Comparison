import math

class Node:
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        if name is None:
            name = f"N({self.x},{self.y})"
        self.name = name
        self.edges = []
    
    def __str__(self):
        return f"Node at ({self.x},{self.y})"
    
    def connect_to_node(self, target_node):
        new_edge = Edge(self, target_node)
        self.edges.append(new_edge)
        target_node.edges.append(new_edge)


class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.weight = self.edge_length()
    
    def __str__(self):
        return f"Edge connecting {self.start.name} to {self.end.name}"
    
    def edge_length(self):
        return math.sqrt((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2)
