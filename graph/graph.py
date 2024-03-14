from graph.node import Node


class Graph:
    def __init__(self):
        self.nodes = set()

    def add_node(self, origin: Node, value, link_value=1):
        target = Node(value)
        origin.link(target, link_value)
        self.nodes.add(target)
        return target

    def add_link(self, origin: Node, target: Node, value=1):
        origin.link(target, value)

    def find_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None
