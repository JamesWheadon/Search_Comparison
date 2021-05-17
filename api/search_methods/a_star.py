from api.search_methods.reverse_a_star import ReverseAStarVertex
from errors import PositionError # type: ignore
from tree import Tree, TreeNode # type: ignore
from reverse_a_star import ReverseAStar # type: ignore
from graph import Graph #type: ignore
import math
from operator import attrgetter

class AStarSearch:
    def __init__(self, graph, start, target, heuristic_method):
        self.map = graph
        self.start = start
        self.target = target
        self.h_method = heuristic_method
        self.tree = Tree
        self.new_node = TreeNode
        self.expanded_nodes = []
        self.potential_nodes = []
        self.completed = False
        self.path = []
        self.reverse_search = None
    
    def find_start(self):
        start_node = self.map.find_node(self.start[0], self.start[1])
        if start_node:
            self.start = start_node
            self.expanded_nodes.append(start_node)
            start = TreeNode(AStarVertex(start_node, 0, self.target, self.h_method, self.reverse_search))
            self.new_node = start
            self.tree = Tree(start)
        else:
            raise PositionError(self.start)
    
    def find_target(self):
        target_node = self.map.find_node(self.target[0], self.target[1])
        if target_node:
            self.target = target_node
        else:
            raise PositionError(self.target)
    
    def expand_vertex(self):
        for edge in self.new_node.value.graph_node.edges:
            if edge.end not in self.expanded_nodes:
                vertex = AStarVertex(edge.end, self.new_node.value.g + edge.weight, self.target, self.h_method, self.reverse_search)
                search_node = self.new_node.add_child(vertex)
                self.potential_nodes.append(search_node)
        self.expanded_nodes.append(self.new_node.value.graph_node)
    
    def new_vertex(self):
        min_f_value = min(self.potential_nodes, key=attrgetter('value.f')).value.f
        min_f_nodes = [node for node in self.potential_nodes if node.value.f == min_f_value]
        max_g_node = max(min_f_nodes, key=attrgetter('value.g'))
        self.new_node = max_g_node
        self.potential_nodes = [node for node in self.potential_nodes if node.value.graph_node != self.new_node.value.graph_node]
        if self.new_node.value.graph_node == self.target:
            self.completed = True
    
    def initialise_search(self):
        target_node = self.map.find_node(self.target[0], self.target[1])
        if target_node:
            self.target = target_node
        else:
            raise PositionError(self.target)
        start_node = self.map.find_node(self.start[0], self.start[1])
        if start_node:
            self.start = start_node
            self.reverse_search = ReverseAStar(self.map, self.start, self.target)
            start = TreeNode(AStarVertex(start_node, 0, self.target, self.h_method, self.reverse_search))
            self.new_node = start
            self.tree = Tree(start)
        else:
            raise PositionError(self.start)
    
    def search(self):
        if self.h_method == 'Reverse':
            self.initialise_search()
        else:
            self.find_target()
            self.find_start()
        while not self.completed:
            self.expand_vertex()
            self.new_vertex()
        self.path = self.new_node.get_path()
        

class AStarVertex:
    def __init__(self, graph_node, distance, target, heuristic, heuristic_search):
        self.graph_node = graph_node
        self.target = target
        self.g = distance
        self.h_search = heuristic_search
        self.heuristic_methods = {'Manhattan': self.manhattan(), 'Euclidean': self.euclidean(), 'Reverse': self.reverse_heuristic()}
        self.h = self.heuristic_methods[heuristic]
        self.f = self.g + self.h
    
    def __str__(self):
        return f"Node: {self.graph_node.name}, distance: {self.f}"
    
    def manhattan(self):
        return abs(self.graph_node.x - self.target.x) + abs(self.graph_node.y - self.target.y)
    
    def euclidean(self):
        return math.sqrt((self.graph_node.x - self.target.x) ** 2 + (self.graph_node.y - self.target.y) ** 2)
    
    def reverse_heuristic(self):
        return self.h_search.find_heuristic(self.graph_node)

graph = Graph([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
search = AStarSearch(graph, (0, 0), (2, 2), 'Reverse')
search.search()
for node in search.path:
    print(node.value)