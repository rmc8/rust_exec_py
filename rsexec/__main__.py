import os
import sys


def main():
    cur_path: str = os.getcwd()
    os.system(f"cd {cur_path}")
    rust_source: str = sys.argv[1]
    os.system(f"rustc {rust_source}")
    os.system(f"./{rust_source[:-3]}")


if __name__ == "__main__":
    main()
