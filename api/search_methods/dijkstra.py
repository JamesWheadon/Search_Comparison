from errors import PositionError
from graph import Graph, Node, Edge
from tree import Tree, TreeNode
from operator import attrgetter

class DijkstraSearch:
    def __init__(self, graph, start, target):
        self.map = graph
        self.start = start
        self.target = target
        self.tree = Tree
        self.new_node = TreeNode
        self.expanded_nodes = []
        self.potential_nodes = []
        self.completed = False
    
    def find_start(self):
        start_node = self.map.find_node(self.start[0], self.start[1])
        if start_node:
            self.start = start_node
            self.expanded_nodes.append(start_node)
            start = TreeNode(DijkstraVertex(start_node, 0))
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
                vertex = DijkstraVertex(edge.end, self.new_node.value.f + edge.weight)
                search_node = self.new_node.add_child(vertex)
                self.potential_nodes.append(search_node)
        self.expanded_nodes.append(self.new_node.value.graph_node)
    
    def new_vertex(self):
        print(self.potential_nodes, self.new_node.value.graph_node, self.target)
        min_f_node = min(self.potential_nodes, key=attrgetter('value.f'))
        self.new_node = min_f_node
        self.potential_nodes = [node for node in self.potential_nodes if node.value.graph_node != self.new_node.value.graph_node]
        if self.new_node.value.graph_node == self.target:
            self.completed = True
    
    def search(self):
        self.find_start()
        self.find_target()
        while not self.completed:
            self.expand_vertex()
            self.new_vertex()

class DijkstraVertex:
    def __init__(self, graph_node, distance):
        self.graph_node = graph_node
        self.f = distance
    
    def __str__(self):
        return f"Node: {self.graph_node.name}, distance: {self.f}"

graph = Graph([[1, 1], [1, 1]])
search = DijkstraSearch(graph, (0, 0), (1, 1))
search.search()
search.tree.render_tree()