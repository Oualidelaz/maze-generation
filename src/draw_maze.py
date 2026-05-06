RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
END = "\033[0m"


def draw_maze(matrix, start, end):
    for row in matrix:
        line1 = line2 = right = left = ""
        for cell in row:
            if cell.walls["top"]:
                if sum(cell.walls.values()) == 15:
                    line1 += f"{PURPLE}█████{END}"
                else:
                    line1 += f"█████"
            else:
                if sum(cell.walls.values()) == 15:
                    line1 += f"{PURPLE}█   █{END}"
                else:
                    line1 += "█   █"

            if cell.walls["right"]:
                if sum(cell.walls.values()) == 15:
                    right = f"{PURPLE}█{END}"
                else:
                    right = "█"
            else:
                    right = " "

            if cell.walls["left"]:
                if sum(cell.walls.values()) == 15:
                    left = f"{PURPLE}█{END}"
                else:
                    left = f"█"
            else:
                left = " "

            if cell == start:
                line2 += f"{left}{GREEN}███{END}{right}"
            elif cell == end:
                line2 += f"{left}{RED}███{END}{right}"
            else:
                line2 += f"{left}   {right}"

        print(line1)
        print(line2)        
    print("█" * 5 * len(matrix[0]))
