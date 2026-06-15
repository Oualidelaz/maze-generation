def get_path_positions(path) -> set[tuple[int, int]]:
    path_positions = {(cell.x, cell.y) for cell in path}
    return path_positions