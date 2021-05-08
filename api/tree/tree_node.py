class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        if type(self) == type(child):
            self.children.append(child)
        else:
            raise ChildError('Incompatible child type')


class ChildError(Exception):
    def __init__(self, message):
        self.message = message