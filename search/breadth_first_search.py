from graph.node import Node
from graph.tree import Tree

# initial state: ['o', 'l', 'h', 'e', 'l']
# goal state: ['h', 'e', 'l', 'l', 'o']
# possible actions


def breadth_first_search(start_state, end_state):
    root = Node(start_state)

    node = search_tree(root, end_state)
    if node:
        tree = Tree(root)
        return tree.get_path(node)


def search_tree(root, end_state):
    queued_nodes = [root]
    visited_nodes = set()

    while queued_nodes:
        node = queued_nodes.pop()
        new_nodes = expand_node(node, visited_nodes)

        for new_node in new_nodes:
            if new_node.value == end_state:
                return new_node
            queued_nodes.append(new_node)

        visited_nodes.add(node)

    return None


def get_new_states(state, visited_states):
    new_states = set()
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            new_state = state[:]
            new_state[i], new_state[j] = new_state[j], new_state[i]
            if new_state not in visited_states:
                new_states.add(new_state)

    return new_states


def expand_node(node, visited_nodes):
    state = node.value
    visited_states = set(map(lambda n: n.value, visited_nodes))
    new_states = get_new_states(state, visited_states)
    new_nodes = []

    for new_state in new_states:
        new_nodes.append(node.add_adjacent(Node(new_state)))

    return new_nodes
