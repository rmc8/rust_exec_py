import os
import sys

cur_path: str = os.getcwd()
os.system(f"cd {cur_path}")
rust_source: str = sys.argv[1]
os.system(f"rustc {rust_source}")
os.system(f"./{rust_source[:-3]}")
