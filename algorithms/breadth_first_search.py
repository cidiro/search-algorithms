from algorithms.strategy import Strategy
from graph.node import Node
from graph.tree import Tree


class BreadthFirstSearch(Strategy):
    def solve(self, start_state, end_state, produce_new_states):
        self.tree = Tree(Node(start_state))
        self.end_state = end_state
        self.produce_new_states = produce_new_states
        self.visited_nodes = set()

        node = self.build_search_tree()
        if node:
            return self.tree.find_path(node)
        return None

    def build_search_tree(self):
        queued_nodes = [self.tree.root]

        while queued_nodes:
            node = queued_nodes.pop()
            # print(str(node) + " - parent: " + str(node.get_parent()))
            new_nodes = self.expand_node(node)

            for new_node in new_nodes:
                if new_node.value == self.end_state:
                    return new_node
                queued_nodes.append(new_node)

            self.visited_nodes.add(node)

        return None

    def expand_node(self, node):
        state = node.value
        visited_states = set(map(lambda n: n.value, self.visited_nodes))
        new_states = self.produce_new_states(state)

        # Removes visited states from new states using set for effeciency
        new_states = [x for x in new_states if x not in visited_states]

        # print("State: " + str(state)
        #       + " - New states: " + str(new_states)
        #       + " - Visited states: " + str(visited_states))

        # convert new states into new nodes
        new_nodes = [node.add_adjacent(Node(new_state))
                     for new_state in new_states]

        return new_nodes
