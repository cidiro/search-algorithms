from algorithms.strategy import Strategy
from graph.tree import Tree


class GreedyBestFirstSearch(Strategy):
    def __init__(self):
        super().__init__()
        self.has_heuristic = True

    def solve(self, start_state, is_goal_state, produce_new_states):
        self.tree = Tree(start_state)
        self.is_goal_state = is_goal_state
        self.produce_new_states = produce_new_states

        node = self.build_search_tree()
        if node:
            return self.tree.find_path(node)
        return None

    def build_search_tree(self):
        self.seen_nodes.add(self.tree.root)
        new_nodes = self.expand_node(self.tree.root)

        while new_nodes:
            for new_node in new_nodes:
                if self.is_goal_state(new_node.value):
                    return new_node
                self.seen_nodes.add(new_node)

            node = min(new_nodes, key=lambda n: n.value.heuristic)
            new_nodes = self.expand_node(node)

            self.watch_node = node  # Watch current node
        return None

    def expand_node(self, node):
        state = node.value
        seen_states = set(map(lambda n: n.value, self.seen_nodes))
        new_states = self.produce_new_states(state)

        # Removes visited states from new states using set for effeciency
        new_states = [x for x in new_states if x not in seen_states]

        # convert new states into new nodes
        new_nodes = [self.tree.add_node(parent=node, value=new_state)
                     for new_state in new_states]

        return new_nodes
