import os
import sys
import subprocess


def exit_if(exit_sw: bool, text: str):
    if exit_sw:
        print(text)
        exit()


def yn_input() -> bool:
    while True:
        choice = input("Please respond with 'yes' or 'no' [y/N]: ").lower()
        if choice in ["y", "ye", "yes"]:
            return True
        elif choice in ["n", "no", "exit"]:
            return False


def del_old_files(path: str):
    del_extension_list: list = ["exe", "pdb"]
    for extension in del_extension_list:
        del_path : str = f"{path}.{extension}"
        if os.path.exists(del_path):
            os.remove(del_path)
            print(f"del {del_path}")


def main():
    cur_path: str = os.getcwd()
    os.system(f"cd {cur_path}")
    exit_if(
        len(sys.argv) == 1,
        "No arguments were found that contain the path to the .rs script",
    )
    rust_source: str = sys.argv[1]
    exit_if(rust_source[-3:] != ".rs", "No .rs extension")
    cmd_lines : list = [f"rustc {rust_source}", f".\\{rust_source[:-3]}", ]
    if os.path.exists(f"{cur_path}\\{rust_source[:-3]}.exe"):
        print(f"The {rust_source[:-3]}.exe already exists. Do you want to overwrite it and run it?")
        if not yn_input():
            exit()
        del_old_files(rust_source[:-3])
    for cmd in cmd_lines:
        print(cmd)
        subprocess.call(cmd)


if __name__ == "__main__":
    main()
