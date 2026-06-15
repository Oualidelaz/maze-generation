import sys
import os
from pathlib import Path

RED = "\033[0;31m"
END = "\033[0m"


def parser(key, value):
    data = dict()
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
        
    if key.lower() == "perfect":
        if isinstance(value, bool):
            return {key.upper(): value}
        if isinstance(value, str):
            value = value.strip().lower()
            if value == "true":
                return {key.upper(): True}
            elif value == "false":
                return {key.upper(): False}
            raise ValueError(f"Invalid value '{value}' for '{key}'. Expected 'True' or 'False'.")
        raise TypeError(f"Invalid type '{type(value).__name__}' for '{key}'. Expected a boolean.")

    else:
        raise ValueError(f"Unknown key: {key}")
def parsing():
    try:
        if len(sys.argv) == 2:
            result = dict()
            FILE = sys.argv[1]
            file_path = Path(FILE)
            if os.path.isfile(file_path) and FILE.endswith('.txt'):
                try:
                    with open(file_path, "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            line = line.strip() 
                            if not line or line.startswith("#") or line == "":
                                continue
                            else:
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
                                    item = parser(key, value)
                                    if item:
                                        result.update(item)
                                except Exception as e:
                                    raise ValueError(e)
                        return result
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
