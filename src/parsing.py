import sys
import os
from pathlib import Path

RED = "\033[0;31m"
END = "\033[0m"


def parser(key, value):
    if key.lower() == "height" or key.lower() == "width":

        try:
            num = int(value)
        except ValueError:
            raise ValueError(f"Invalid {key.lower()} value: '{value}' must be an integer.")
        
        if num < 0:
            raise ValueError(f"{key.capitalize()} cannot be negative, got {num}.")
        if num >= 500:
            raise ValueError(f"{key.capitalize()}: {num} is too large!")
        return {key.upper(): num}


    if key.lower() == "entry":
        try:
            x, y = value.split(',')
        except ValueError:
            raise ValueError("Value unpacking failed. ENTRY must be 'x,y' format")
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            raise ValueError(f"Invalid coordinates: x='{x}' and y='{y}' must both be integers.")
        return {key.upper(): (x, y)}
        

    if key.lower() == "exit":
        try:
            x, y = value.split(',')
        except ValueError:
            raise ValueError("Value unpacking failed. EXIT must be 'x,y' format")
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            raise ValueError(f"Invalid coordinates: x='{x}' and y='{y}' must both be integers.")
        return {key.upper(): (x, y)}
        

    raise ValueError(f"Unknown key: '{key}'.")



try:
    if len(sys.argv) == 2:
        result = dict()
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
                        data = clean_line.split('=')
                        try:
                            key, value = data[0], data[1]
                            if parser(key, value):
                                result.update({key, value})
                        except Exception:
                            raise ValueError("config must contain key and value")
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
