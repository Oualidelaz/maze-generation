RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
YELLOW = "\033[1;33m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
LIGHT_RED = "\033[1;31m"
END = "\033[0m"


def draw_maze(matrix, start, end, color, path_coordinates=None):
    for row in matrix:
        line1 = line2 = right = left = ""
        for cell in row:
            if cell.walls["top"]:
                if sum(cell.walls.values()) == 15:
                    line1 += f"{PURPLE}█████{END}"
                else:
                    if color == "CYAN":
                        line1 += f"{CYAN}█████{END}"
                    elif color == "BLUE":
                        line1 += f"{BLUE}█████{END}"
                    elif color == "YELLOW":
                        line1 += f"{YELLOW}█████{END}"
                    elif color == "LIGHT_GRAY":
                        line1 += f"{LIGHT_GRAY}█████{END}"
                    else:
                        line1 += f"█████"
            else:
                if sum(cell.walls.values()) == 15:
                    line1 += f"{PURPLE}█   █{END}"
                else:
                    if color == "CYAN":
                        line1 += f"{CYAN}█   █{END}"
                    elif color == "BLUE":
                        line1 += f"{BLUE}█   █{END}"
                    elif color == "YELLOW":
                        line1 += f"{YELLOW}█   █{END}"
                    elif color == "LIGHT_GRAY":
                        line1 += f"{LIGHT_GRAY}█   █{END}"
                    else:
                        line1 += "█   █"

            if cell.walls["right"]:
                if sum(cell.walls.values()) == 15:
                    right = f"{PURPLE}█{END}"
                else:
                    if color == "CYAN":
                        right = f"{CYAN}█{END}"
                    elif color == "BLUE":
                        right = f"{BLUE}█{END}"
                    elif color == "YELLOW":
                        right = f"{YELLOW}█{END}"
                    elif color == "LIGHT_GRAY":
                        right = f"{LIGHT_GRAY}█{END}"
                    else:
                        right = "█"
            else:
                    right = " "

            if cell.walls["left"]:
                if sum(cell.walls.values()) == 15:
                    left = f"{PURPLE}█{END}"
                else:
                    if color == "CYAN":
                        left = f"{CYAN}█{END}"
                    elif color == "BLUE":
                        left = f"{BLUE}█{END}"
                    elif color == "YELLOW":
                        left = f"{YELLOW}█{END}"
                    elif color == "LIGHT_GRAY":
                        left = f"{LIGHT_GRAY}█{END}"
                    else:
                        left = "█"
            else:
                left = " "

            if cell == start:
                line2 += f"{left}{GREEN}███{END}{right}"
            elif cell == end:
                line2 += f"{left}{RED}███{END}{right}"
            elif path_coordinates is not None and (cell.x, cell.y) in path_coordinates:
                line2 += f"{left}{LIGHT_RED}███{END}{right}"
            else:
                line2 += f"{left}   {right}"

        print(line1)
        print(line2)
    if color == "CYAN":
        print(f"{CYAN}█{END}" * 5 * len(matrix[0]))
    elif color == "BLUE":
        print(f"{BLUE}█{END}" * 5 * len(matrix[0]))
    elif color == "YELLOW":
        print(f"{YELLOW}█{END}" * 5 * len(matrix[0]))
    elif color == "LIGHT_GRAY":
        print(f"{LIGHT_GRAY}█{END}" * 5 * len(matrix[0]))
    else:
        print("█" * 5 * len(matrix[0]))
