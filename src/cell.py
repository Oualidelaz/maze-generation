class Cell:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.visited = False
        self.walls = {
            'top': 1,
            'right': 2,
            'bottom': 4,
            'left':8
        }
