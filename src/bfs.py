def bfs(matrix, entry, exit, width, height):
    start = matrix[entry[1]][entry[0]]
    end = matrix[exit[1]][exit[0]]
    queue = [start]
    visited = set()
    parent = {start: None}
    while queue:
        current = queue.pop(0)
        if current == end:
            break
        visited.add(current)
        neighbors = {
            "top": (current.x, current.y - 1),
            "bottom": (current.x, current.y + 1),
            "left": (current.x - 1, current.y),
            "right": (current.x + 1, current.y),
        }
        for direction, (x, y) in neighbors.items():
            if 0 <= x < width and 0 <= y < height:
                neighbor = matrix[y][x]
                if (neighbor not in visited
                    and current.walls[direction] == 0):
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
    path = []
    if end not in parent:
        return path
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path
