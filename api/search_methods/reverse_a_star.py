from errors import PositionError # type: ignore
from operator import attrgetter
import sqlite3

class ReverseAStar:
    def __init__(self, graph, target):
        self.map = graph
        self.target = target
        self.expanded_nodes = []
        self.potential_nodes = []
        self.completed = False
        self.path = []
    
    def initialise_db(self):
        connection = sqlite3.connect('reverse.db')
        with open('./api/search_methods/schema.sql') as schema:
            connection.executescript(schema.read())
        connection.commit()
        connection.close()
    
    def connecto_to_db(self):
        db = sqlite3.connect('reverse.db')
        return db
    
    def expand_vertex(self):
        for edge in self.new_node.graph_node.edges:
            if edge.end not in self.expanded_nodes:
                vertex = ReverseAStarVertex(edge.end, self.new_node.g + edge.weight, self.target)
                self.potential_nodes.append(vertex)
        self.expanded_nodes.append(self.new_node.graph_node)
    
    def new_vertex(self):
        min_f_value = min(self.potential_nodes, key=attrgetter('f')).f
        min_f_nodes = [node for node in self.potential_nodes if node.f == min_f_value]
        max_g_node = max(min_f_nodes, key=attrgetter('g'))
        self.new_node = max_g_node
        self.potential_nodes = [node for node in self.potential_nodes if node.graph_node != self.new_node.graph_node]
        if self.new_node.graph_node == self.target:
            self.completed = True


class ReverseAStarVertex:
    def __init__(self, graph_node, distance, target):
        self.graph_node = graph_node
        self.g = distance
        self.h = self.manhattan(target)
        self.f = self.g + self.h
    
    def __str__(self):
        return f"Node: {self.graph_node.name}, distance: {self.f}"
    
    def manhattan(self, target_node):
        return abs(self.graph_node.x - target_node.x) + abs(self.graph_node.y - target_node.y)