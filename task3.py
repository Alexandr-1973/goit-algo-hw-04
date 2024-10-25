import sys
from pathlib import Path
from colorama import Fore

def iter_directory_colours(directory, start_stick=""):
    directory_list = list(directory)
    for index, path in enumerate(directory_list):
        name_item = Path(path)
        if index == len(directory_list) - 1:
            last_stick = "┗ "
            new_start_stick = start_stick + "  "
        else:
            last_stick = "┣ "
            new_start_stick = start_stick + "┃ "
        if name_item.is_dir():
            print(f"{start_stick}{last_stick}📂{Fore.BLUE}{name_item.name}{Fore.RESET}")
            iter_directory_colours(name_item.iterdir(), new_start_stick)
        else:
            print(f"{start_stick}{last_stick}📜{Fore.GREEN}{name_item.name}{Fore.RESET}")

def main():
    if sys.argv[1] and Path(sys.argv[1]).is_dir():
        print(f"📦{Fore.YELLOW}{sys.argv[1]}{Fore.RESET}")
        test_dir = Path(sys.argv[1]).iterdir()
        iter_directory_colours(test_dir)
    else:
        print("No directory")
        return

main()
