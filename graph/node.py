from graph.link import Link


class Node:
    def __init__(self, value):
        self.value = value
        self.links = []

    def add_adjacent(self, node, link_value):
        self.links.append(Link(self, node, link_value))

    def remove_link(self, link):
        self.links.remove(link)

    def __str__(self):
        return f"Node({self.value})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)
