class Tree:
    def __init__(self, root):
        self.root = root

    def add_node(self, parent, child, link_value=1):
        parent.add_adjacent(child, link_value)
        return child

    def get_path(self, node):
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]
