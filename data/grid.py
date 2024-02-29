class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]

    def position_is_valid(self, p):
        return 0 <= p.x < self.width and 0 <= p.y < self.height
