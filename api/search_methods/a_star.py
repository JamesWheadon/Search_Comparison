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
    
    def expand_vertex(self):
        for edge in self.new_node.value.graph_node.edges:
            if edge.end not in self.expanded_nodes:
                vertex = AStarVertex(edge.end, self.new_node.value.g + edge.weight, self.target, 'Manhattan')
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
    
    def search(self):
        self.find_target()
        self.find_start()
        while not self.completed:
            self.expand_vertex()
            self.new_vertex()
        self.path = self.new_node.get_path()
        

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

graph = Graph([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
search = AStarSearch(graph, (0, 0), (2, 2))
search.search()
for node in search.path:
    print(node.value.graph_node, node.value.f)
search.tree.render_tree()