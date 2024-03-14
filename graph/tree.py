from graph.node import Node
import networkx as nx
import matplotlib.pyplot as plt


class Tree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def add_node(self, parent: Node, value, link_value=1):
        child = Node(value)
        parent.link(child, link_value)
        return child

    def find_path_to_node(self, upper_node: Node, lower_node: Node):
        path = []
        while lower_node is not upper_node:
            path.append(lower_node)
            lower_node = lower_node.get_parent()
            if lower_node is None:
                return None
        path.append(upper_node)
        path.reverse()
        return path

    def find_path(self, node: Node):
        return self.find_path_to_node(self.root, node)

    def max_depth(self):
        def dfs(node, depth):
            if not node or not node.get_children():
                return depth
            return max(dfs(child, depth + 1) for child in node.get_children())
        return dfs(self.root, 1)  # Starting with depth 1 for the root

    def visualize(self):
        G = nx.DiGraph()
        self.levels = {}    # Keeps track of levels of nodes
        self.max_level = 0  # Keeps the max level to help in plotting

        # Initialize the process with the root node
        self.__build_networkx_graph(G, self.root, 0)

        # Position nodes to reflect tree structure
        pos = {
            node: (x, -level)
            for level, nodes in self.levels.items()
            for x, node in enumerate(nodes)
        }

        print("Displaying tree...")
        nx.draw(G, pos, with_labels=True, arrows=False,
                node_size=2000, node_color="lightblue",
                font_size=10, font_weight="bold")
        plt.show()

    def __build_networkx_graph(self, G, node, level, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)

        # Assign node to its level
        if level not in self.levels:
            self.levels[level] = []
        self.levels[level].append(node.value)
        self.max_level = max(self.max_level, level)

        # Add the node to the graph
        G.add_node(node.value)

        for link in node.links:
            child = link.target
            if node.value != child.value:
                G.add_edge(node.value, child.value)  # Add edge to the graph

            if child not in visited:
                self.__build_networkx_graph(G, child, level + 1, visited)
