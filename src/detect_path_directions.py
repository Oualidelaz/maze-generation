def detect_path_directions(path_coordinates):
    result = ""
    for current, next in zip(path_coordinates, path_coordinates[1:]):
        current_x = current.x
        current_y = current.y
        next_x = next.x
        next_y = next.y
        dx = next_x - current_x
        dy = next_y - current_y
        if dx == 1:
            result += "E"
        elif dx == -1:
            result += "W"
        if dy == 1:
            result += "S"
        elif dy == -1:
            result += "N"
    return result
