from graph.node import Node


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        return self.nodes[value]

    def add_link(self, source_value, target_value, value):
        source_node = self.add_node(source_value)
        target_node = self.add_node(target_value)
        source_node.add_adjacent(target_node, value)

    def find_node(self, value):
        return self.nodes.get(value, None)
