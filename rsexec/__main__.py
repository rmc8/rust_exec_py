import os
import sys


def exit_if(exit_sw: bool, text: str):
    if exit_sw:
        print(text)
        exit()


def main():
    cur_path: str = os.getcwd()
    os.system(f"cd {cur_path}")
    exit_if(
        len(sys.argv) == 1,
        "No arguments were found that contain the path to the .rs script",
    )
    rust_source: str = sys.argv[1]
    exit_if(rust_source[-3:] != ".rs", "No .rs extension")
    cmd_lines : list = [f"rustc {rust_source}", f"./{rust_source[:-3]}", ]
    for cmd in cmd_lines:
        print(cmd)
        os.system(cmd)


if __name__ == "__main__":
    main()
