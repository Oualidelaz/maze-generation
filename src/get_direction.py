def get_direction(current, neighbor) -> str:
    dx = neighbor.x - current.x
    dy = neighbor.y - current.y

    if dx == -1:
        return 'top'
    if dx == 1:
        return 'bottom'
    if dy == -1:
        return 'left'
    if dy == 1:
        return 'right'
    return ""
