from .tree_node import TreeNode

class Tree:
    def __init__(self, root):
        self.root = root
        self.nodes = []
    
    def render_tree(self):
        print(self.root.value)
        if self.root.children:
            for child in self.root.children[:-1]:
                child.render_node(False, "")
            self.root.children[-1].render_node(True, "")