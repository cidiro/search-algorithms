from graph.link import Link


class Node:
    def __init__(self, value):
        self.value = value
        self.links = []

    def add_adjacent(self, node, link_value=1):
        self.links.append(Link(self, node, link_value))
        return node

    def get_children(self):
        children = []
        for link in self.links:
            if link.target != self:
                children.append(link.source)
        return children    

    def get_parents(self):
        parents = []
        for link in self.links:
            if link.source != self:
                parents.append(link.source)
        return parents

    def get_parent(self):
        parents = self.get_parents()
        return return parents[0] if parents else None
        
    def remove_link(self, link):
        self.links.remove(link)
        return link

    def __str__(self):
        return f"Node({self.value})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)
