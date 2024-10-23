from colorama import Fore
import sys
from pathlib import Path

def iter_directory_colours(directory):
    for path in directory:
        if path.is_dir():
            print(f"{Fore.BLUE} {path} {Fore.RESET}")
            iter_directory_colours(Path(path).iterdir())
        else:
            print(f"{Fore.GREEN} {path} {Fore.RESET}")


def main():
    if sys.argv[1] and Path(sys.argv[1]).is_dir():
        test_dir = Path(sys.argv[1]).iterdir()
        iter_directory_colours(test_dir)
    else:
        print("No directory")
        return


main()
