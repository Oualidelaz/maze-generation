from cell import Cell

def generate_matrix(height, width):
    try:
        matrix = [[Cell((x, y)) for x in range(width)] for y in range(height)]
        return matrix
    except Exception:
        raise ValueError("Matrix generating Error!")
