from operator import attrgetter
from graph import Graph #type: ignore
import sqlite3

class ReverseAStar:
    def __init__(self, graph, start, target):
        self.map = graph
        self.start = start
        self.target = target
        self.new_node = ReverseAStarVertex
        self.expanded_nodes = []
        self.potential_nodes = []

        self.initialise()
    
    def connecto_to_db(self):
        db = sqlite3.connect('reverse.db')
        cursor = db.cursor()
        return cursor, db
    
    def initialise_db(self):
        cursor, db = self.connecto_to_db()
        with open('./api/search_methods/schema.sql') as schema:
            cursor.executescript(schema.read())
        db.commit()
        db.close()
    
    def expand_vertex(self):
        for edge in self.new_node.graph_node.edges:
            if edge.end not in self.expanded_nodes:
                vertex = ReverseAStarVertex(edge.end, self.new_node.g + edge.weight, self.start)
                self.potential_nodes.append(vertex)
        self.expanded_nodes.append(self.new_node.graph_node)
    
    def new_vertex(self):
        min_f_value = min(self.potential_nodes, key=attrgetter('f')).f
        min_f_nodes = [node for node in self.potential_nodes if node.f == min_f_value]
        max_g_node = max(min_f_nodes, key=attrgetter('g'))
        self.new_node = max_g_node
        self.potential_nodes = [node for node in self.potential_nodes if node.graph_node != self.new_node.graph_node]
        self.update_db()
    
    def update_db(self):
        cursor, db = self.connecto_to_db()
        cursor.execute('INSERT INTO heuristics (node_name, node_h) VALUES (?, ?)', (self.new_node.graph_node.name, self.new_node.g))
        db.commit()
        db.close()
    
    def initialise(self):
        self.initialise_db()
        self.new_node = ReverseAStarVertex(self.target, 0, self.start)
        self.update_db()
    
    def find_heuristic(self, node):
        while node not in self.expanded_nodes:
            self.expand_vertex()
            if self.potential_nodes:
                self.new_vertex()
        cursor, db = self.connecto_to_db()
        for row in cursor.execute('SELECT node_h FROM heuristics WHERE node_name=(?)', (node.name,)):
            return row[0]


class ReverseAStarVertex:
    def __init__(self, graph_node, distance, start):
        self.graph_node = graph_node
        self.g = distance
        self.h = self.manhattan(start)
        self.f = self.g + self.h
    
    def __str__(self):
        return f"Node: {self.graph_node.name}, distance: {self.f}"
    
    def manhattan(self, start_node):
        return abs(self.graph_node.x - start_node.x) + abs(self.graph_node.y - start_node.y)