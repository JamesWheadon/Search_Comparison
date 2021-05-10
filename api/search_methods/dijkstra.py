from errors import PositionError
from graph import Graph, Node, Edge
from tree import Tree, TreeNode

class DijkstraSearch:
    def __init__(self, graph, start, target):
        self.map = graph
        self.start = start
        self.target = target