from graph.node import Node
from graph.tree import Tree


def breadth_first_search(start_state, end_state, produce_new_states):
    root = Node(start_state)

    node = search_tree(root, end_state, produce_new_states)
    if node:
        tree = Tree(root)
        return tree.find_path(node)
    return None


def search_tree(root, end_state, produce_new_states):
    queued_nodes = [root]
    visited_nodes = set()

    while queued_nodes:
        node = queued_nodes.pop()
        # print(str(node) + " - parent: " + str(node.get_parent()))
        new_nodes = expand_node(node, visited_nodes, produce_new_states)

        for new_node in new_nodes:
            if new_node.value == end_state:
                return new_node
            queued_nodes.append(new_node)

        visited_nodes.add(node)

    return None


def expand_node(node, visited_nodes, produce_new_states):
    state = node.value
    visited_states = set(map(lambda n: n.value, visited_nodes))

    new_states = produce_new_states(state) - visited_states

    # print("State: " + str(state)
    #       + " - New states: " + str(new_states)
    #       + " - Visited states: " + str(visited_states))

    # convert new states into new nodes
    new_nodes = [node.add_adjacent(Node(new_state))
                 for new_state in new_states]

    return new_nodes
