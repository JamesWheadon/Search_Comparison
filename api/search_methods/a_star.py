from errors import PositionError # type: ignore
from graph import Graph #type: ignore
from tree import Tree, TreeNode # type: ignore
from operator import attrgetter

class AStarSearch:
    def __init__(self, graph, start, target):
        self.map = graph
        self.start = start
        self.target = target
        self.tree = Tree
        self.new_node = TreeNode
        self.expanded_nodes = []
        self.potential_nodes = []
        self.completed = False
        self.path = []
    
    def find_start(self):
        start_node = self.map.find_node(self.start[0], self.start[1])
        if start_node:
            self.start = start_node
            self.expanded_nodes.append(start_node)
            start = TreeNode(AStarVertex(start_node, 0, self.target, 'Manhattan'))
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
    
    def search(self):
        self.find_target()
        self.find_start()
        

class AStarVertex:
    def __init__(self, graph_node, distance, target, heuristic):
        self.heuristic_methods = {'Manhattan': self.manhattan}
        self.graph_node = graph_node
        self.g = distance
        self.h = self.heuristic_methods[heuristic](graph_node, target)
        self.f = self.g + self.h
    
    def __str__(self):
        return f"Node: {self.graph_node.name}, distance: {self.f}"
    
    def manhattan(self, start_node, target_node):
        return abs(start_node.x - target_node.x) + abs(start_node.y - target_node.y)
