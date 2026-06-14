import sys
import os
import random
import time
from parsing import parsing
from generate_matrix import generate_matrix
from dfs import dfs
from add_loops import add_loops
from draw_maze import draw_maze
from trace_u import trace_u


def run(data, color, mtx=None):                
    height = data.get("HEIGHT")
    width = data.get("WIDTH")
    entry = data.get("ENTRY")
    exit = data.get("EXIT")
    perfect = data.get("PERFECT")
    if mtx is not None:
        matrix = mtx
    else:
        matrix = generate_matrix(height, width)
    trace_u(matrix, height, width, entry, exit)
    dfs(matrix, entry, height, width)
    if perfect and mtx is None:
        add_loops(matrix, height, width)
    start_cell = matrix[entry[1]][entry[0]]
    exit_cell = matrix[exit[1]][exit[0]]
    draw_maze(matrix, start_cell, exit_cell, color)
    return matrix


def display_menu():
    print("""
==============================
         MAZE MENU
==============================

[1] Draw Maze
[2] Change Maze Color
[3] Show Maze Path

[0] Exit

==============================""")



def main():
    RED = "\033[0;31m"
    YELLOW = "\033[1;33m"
    END = "\033[0m"
    try:
        colors = ["CYAN", "BLUE", "YELLOW", "LIGHT_GRAY"]
        current_color = "white"
        data = parsing()
        matrix = None
        os.system("cls") if os.name == "nt" else os.system("clear")
        while True:
            display_menu()
            try:
                choice = int(input("Choose an option: "))
                if choice not in (0, 1, 2, 3):
                    raise ValueError
            except ValueError:
                print(f"\n{RED}[!] Invalid choice!{END}")
                time.sleep(0.5)
            
            os.system("cls") if os.name == "nt" else os.system("clear")
            if choice == 1:
                matrix = run(data, current_color)
            elif choice == 2:
                available_colors = [color for color in colors if color != current_color]
                current_color = random.choice(available_colors)
                if matrix is not None:
                    run(data, current_color, matrix)
                else:
                    run(data, current_color)
            elif choice == 3:
                run(data, current_color)
                # show path
            elif choice == 0:
                print(f"{YELLOW}[*] Exiting Maze Program... Goodbye!{END}")
                sys.exit()

    except KeyboardInterrupt:
        print(f"\n{RED}[!] Interrupted by user. Exiting gracefully...{END}")
        sys.exit()
    except Exception:
        print(f"\n{RED}[!] Something Wrong!{END}")
        sys.exit()
main()
