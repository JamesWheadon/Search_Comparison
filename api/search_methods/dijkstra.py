from errors import PositionError
from graph import Graph, Node, Edge
from tree import Tree, TreeNode

class DijkstraSearch:
    def __init__(self, graph, start, target):
        self.map = graph
        self.start = start
        self.target = target
    
    def find_start(self):
        start_node = self.map.find_node(self.start[0], self.start[1])
        if start_node:
            self.start = start_node
        else:
            raise PositionError(self.start)
    
    def find_target(self):
        target_node = self.map.find_node(self.target[0], self.target[1])
        if target_node:
            self.start = target_node
        else:
            raise PositionError(self.target)
    
    def search(self):
        self.find_start()
        self.find_target()
    

graph = Graph([[1, 1], [1, 1]])
search = DijkstraSearch(graph, (0, 0), (1, 2))
search.search()