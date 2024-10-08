from algorithms.strategy import Strategy
from graph.tree import Tree


class UniformCostSearch(Strategy):
    def solve(self, start_state, is_goal_state, produce_new_states):
        self.tree = Tree(start_state)
        self.is_goal_state = is_goal_state
        self.produce_new_states = produce_new_states

        node = self.build_search_tree()
        if node:
            return self.tree.find_path(node)
        return None

    def build_search_tree(self):
        node_queue = [self.tree.root]
        self.seen_nodes.add(self.tree.root)

        while node_queue:
            node = min(node_queue, key=lambda n: n.value.cost)
            # print node_queue
            print(f"Node queue: {[f'{str(n.value)}:{str(n.value.cost)}' for n in node_queue]}")
            print(f"Min node: {node.value} with cost: {node.value.cost}")
            node_queue.remove(node)
            if self.is_goal_state(node.value):
                return node

            new_nodes = self.expand_node(node)
            for new_node in new_nodes:
                node_queue.append(new_node)
                self.seen_nodes.add(new_node)

            self.watch_node = node  # Watch current node
        return None

    def expand_node(self, node):
        state = node.value
        seen_states = set(map(lambda n: n.value, self.seen_nodes))
        new_states = self.produce_new_states(state)

        # Removes visited states from new states using set for effeciency
        new_states = [x for x in new_states if x not in seen_states]

        # Update cost of new states
        for new_state in new_states:
            new_state.cost += state.cost

        print(f"{state} -> {[f"{str(s)}:{str(s.cost)}" for s in new_states]}")

        # convert new states into new nodes
        new_nodes = [self.tree.add_node(parent=node, value=new_state)
                     for new_state in new_states]

        return new_nodes
