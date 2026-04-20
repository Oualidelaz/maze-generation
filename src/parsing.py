import sys
import os
from pathlib import Path

RED = "\033[0;31m"
END = "\033[0m"

try:
    if len(sys.argv) == 2:
        FILE = sys.argv[1]
        file_path = Path(FILE)
        if os.path.isfile(file_path) and FILE.endswith('.txt'):
            try:
                with open(file_path, "r") as file:
                    for line in file:
                        stripped = line.strip()
                        if not stripped or stripped.startswith("#"):
                            continue
                        ln = line.split('#', 1)[0].strip()
                        clean_line = ""
                        for character in ln:
                            if character in (" ", "\t", "\v"):
                                continue
                            clean_line += character
                        if '=' not in clean_line:
                            raise ValueError(f"{RED}Invalid format: expected 'key=value'{END}")
            except ValueError as e:
                print(e)
                sys.exit(1)
            except OSError as e:
                print(f"{RED}File error: {e}{END}")
                sys.exit(1)
        else:
            print(f"{RED}File not found or not a valid file: '{file_path}'{END}")
            sys.exit(1)
    else:
        print(f"{RED}Usage Example: <maze.py config.txt>{END}")
        sys.exit(1)

except Exception as e:
    print(f"{RED}Unexpected error: {e}{END}")
    sys.exit(1)
