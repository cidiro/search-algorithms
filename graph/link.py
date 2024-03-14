class Link:
    def __init__(self, origin, target, value):
        self.origin = origin
        self.target = target
        self.value = value

    def __str__(self):
        return f"Link({self.origin}, {self.target}, {self.value})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.origin == other.origin
                and self.target == other.target
                and self.value == other.value
                )

    def __hash__(self):
        return id(self)
