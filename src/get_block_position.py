from cell_closed import coordinates

def get_block_position(height, width):
    cell_closed = coordinates()
    if height is not None and width is not None:
        middle_x = width // 2
        middel_y = height // 2
    else:
        raise ValueError("width and height must both be integers")
    blocked = set()
    for bx, by in cell_closed:
        dx = middle_x + bx
        dy = middel_y + by
        if 0 <= dx < width and 0 <= dy < height:
            blocked.add((dx, dy))
    return blocked
