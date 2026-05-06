from parsing import parsing
from generate_matrix import generate_matrix
from dfs import dfs
from add_loops import add_loops
from draw_maze import draw_maze
from trace_u import trace_u

def main():
    try:
        data = parsing()
        height = data.get("HEIGHT")
        width = data.get("WIDTH")
        entry = data.get("ENTRY")
        exit = data.get("EXIT")
        perfect = data.get("PERFECT")
        matrix = generate_matrix(height, width)
        trace_u(matrix, height, width, entry, exit)
        dfs(matrix, entry, height, width)
        if perfect:
            add_loops(matrix, height, width)
        start_cell = matrix[entry[1]][entry[0]]
        exit_cell = matrix[exit[1]][exit[0]]
        draw_maze(matrix, start_cell, exit_cell)
    except Exception as e:
        print(e)
main()
