class Link:
    def __init__(self, source, target, value):
        self.source = source
        self.target = target
        self.value = value

    def __str__(self):
        return f"Link({self.source}, {self.target}, {self.value})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return (self.source == other.source
                and self.target == other.target
                and self.value == other.value
                )

    def __hash__(self):
        return id(self)
