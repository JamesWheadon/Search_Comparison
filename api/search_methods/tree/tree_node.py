class TreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.depth = 0
    
    def add_child(self, child):
        if type(self.value) == type(child):
            child_node = TreeNode(child)
            child_node.depth = self.depth + 1
            self.children.append(child_node)
            return child_node
        else:
            raise ChildError
    
    def render_node(self, last_child, previous):
        if last_child:
            print(previous + u'\u2514\u2500' + f"{self.value}")
            children_previous = previous + u'   '
        else:
            print(previous + u'\u251c\u2500' + f"{self.value}")
            children_previous = previous + u'\u2502  '
        if self.children:
            for child in self.children[:-1]:
                child.render_node(False, children_previous)
            self.children[-1].render_node(True, children_previous)


class ChildError(Exception):
    def __init__(self):
        self.message = 'Incompatible child type'
        super().__init__(self.message)