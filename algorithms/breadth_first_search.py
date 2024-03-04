from algorithms.strategy import Strategy
from graph.node import Node
from graph.tree import Tree


class BreadthFirstSearch(Strategy):
    def solve(self, start_state, end_state, produce_new_states):
        self.tree = Tree(Node(start_state))
        self.end_state = end_state
        self.produce_new_states = produce_new_states
        self.seen_nodes = set()

        node = self.build_search_tree()
        if node:
            return self.tree.find_path(node)
        return None

    def build_search_tree(self):
        node_queue = [self.tree.root]
        self.seen_nodes.add(self.tree.root)

        while node_queue:
            node = node_queue.pop(0)
            new_nodes = self.expand_node(node)

            for new_node in new_nodes:
                if new_node.value == self.end_state:
                    return new_node
                node_queue.append(new_node)
                self.seen_nodes.add(new_node)

        return None

    def expand_node(self, node):
        state = node.value
        seen_states = set(map(lambda n: n.value, self.seen_nodes))
        new_states = self.produce_new_states(state)

        # Removes visited states from new states using set for effeciency
        new_states = [x for x in new_states if x not in seen_states]

        # convert new states into new nodes
        new_nodes = [node.add_adjacent(Node(new_state))
                     for new_state in new_states]

        return new_nodes
