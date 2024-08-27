from graph.node import Node
import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self):
        self.nodes = set()

    def add_node(self, value):
        node = Node(value)
        self.nodes.add(node)
        return node

    def add_link(self, origin: Node, target: Node, value=1):
        return origin.link(target, value)

    def add_node_linked(self, origin: Node, value, link_value=1):
        target = Node(value)
        origin.link(target, link_value)
        self.nodes.add(target)
        return target

    def get_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def get_link(self, origin: Node, target: Node):
        for link in origin.links:
            if link.origin is origin:
                if link.target == target:
                    return link
            else:
                if link.origin == target:
                    return link
        return None

    def visualize(self):
        plt.figure(figsize=(8, 8))
        G = nx.DiGraph()
        for node in self.nodes:
            G.add_node(node.value)
            for link in node.links:
                G.add_edge(link.origin.value,
                           link.target.value,
                           weight=link.value)

        pos = nx.shell_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000,
                edge_color='k', linewidths=1, font_size=15, arrows=True)
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels={(u, v): d['weight']
                                 for u, v, d in G.edges(data=True)}
        )
        plt.show()
