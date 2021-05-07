class Node:
    def __init__(self, x, y, name=None):
        self.x = x
        self.y = y
        self.name = name
        self.edges = []
    
    def __str__(self):
        return f"Node at ({self.x}, {self.y})"


class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        return f"Edge connecting {start.name} to {end.name}"
