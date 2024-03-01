from graph.link import Link


class Node:
    def __init__(self, value):
        self.value = value
        self.links = []

    def add_adjacent(self, node, link_value=1):
        link = Link(self, node, link_value)
        self.links.append(link)
        node.links.append(link)
        return node

    def get_children(self):
        return [link.target for link in self.links
                if link.target is not self]

    def get_parents(self):
        return [link.source for link in self.links
                if link.source is not self]

    def get_parent(self):
        parents = self.get_parents()
        return (parents[0] if parents else None)

    def remove_link(self, link):
        self.links.remove(link)
        return link

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return id(self)
