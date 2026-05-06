def get_direction(current, neighbor) -> str:
    dx = neighbor.x - current.x
    dy = neighbor.y - current.y

    if dy == -1:
        return 'top'
    if dy == 1:
        return 'bottom'
    if dx == -1:
        return 'left'
    if dx == 1:
        return 'right'
    return ""
