from cell_closed import coordinates

def trace_u(matrix, height, width, entry, exit):
    cell_closed = coordinates()
    middle_x = width // 2
    middle_y = height // 2

    if (entry[0] - middle_x, entry[1] - middle_y) in cell_closed:
        raise ValueError("Entry cannot be inside U shape")

    if (exit[0] - middle_x, exit[1] - middle_y) in cell_closed:
        raise ValueError("Exit cannot be inside U shape")

    for current_x, current_y in cell_closed:
        x = current_x + middle_x
        y = current_y + middle_y
        if 0 <= x < width and 0 <= y < height:
            cell = matrix[y][x]
            cell.visited = True
