import random
from get_direction import get_direction
from get_block_position import get_block_position

def add_loops(matrix, height, width):
    cell_closed =  get_block_position(height, width)
    for row in matrix:
        for current in row:
            x = current.x
            y = current.y
            neighbors = {
                "top": (x, y - 1),
                "bottom": (x, y + 1),
                "left": (x - 1, y),
                "top": (x + 1, y)
            }
            valid_neighbors = []
            for nx, ny in neighbors.values():
                if 0 <= nx < width and 0 <= ny < height:
                    cell = matrix[ny][nx]
                    if cell.visited and (x, y) not in cell_closed and (nx, ny) not in cell_closed:
                        valid_neighbors.append(cell)
            if valid_neighbors:
                if random.random() < 0.10:
                    neighbor = random.choice(valid_neighbors)
                    current_dir = get_direction(current, neighbor)
                    neighbor_dir = get_direction(neighbor, current)
                    current.walls[current_dir] = 0
                    neighbor.walls[neighbor_dir] = 0
