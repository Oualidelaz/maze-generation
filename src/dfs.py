import random
from .get_direction import get_direction

def dfs(self, matrix):
    stack = []
    entry_x, entry_y = self.entry
    n_cell = matrix[entry_y][entry_x]
    n_cell.visited = True
    stack.append(n_cell)

    while stack:
        current = stack[-1]
        x, y = current.x, current.y
        valid_neighbors = []
        neighbors = {
            'top': (x, y - 1),
            'down': (x, y + 1),
            'left': (x - 1, y),
            'right': (x + 1, y),
        }
        for nx, ny in neighbors.values():
            if 0 <= nx < self.width and 0 <= ny < self.height: 
                cell = matrix[ny][nx]
                if not cell.visited:
                    valid_neighbors.append(cell)
    
        if valid_neighbors:
            neighbor = random.choice(valid_neighbors)
            direction = get_direction(current, neighbor)
            opposite_direction  = get_direction(neighbor, current)
            current.walls[direction] = 0
            neighbor.walls[opposite_direction] = 0
            neighbor.visited = True
            stack.append(neighbor)
        else:
            stack.pop()
