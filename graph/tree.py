from graph.node import Node


class Tree:
    def __init__(self, root):
        self.root = root

    def add_node(self, parent, child_value, link_value=1):
        child = Node(child_value)
        parent.add_adjacent(child, link_value)
        return child

    def find_path_to_node(self, upper_node, lower_node):
        path = []
        while lower_node is not upper_node:
            path.append(lower_node)
            lower_node = lower_node.get_parent()
            if lower_node is None:
                return None
        path.append(upper_node)
        path.reverse()
        return path

    def find_path(self, node):
        return self.find_path_to_node(self.root, node)

    
