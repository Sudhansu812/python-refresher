import os
from os import path
from pathlib import Path

sample_file: Path = Path(r"./Sample.txt")
file_modes: Path = Path(r"./file_modes.txt")
bin_file: Path = Path(r"./bin_file.bin")


if path.exists(sample_file):
    os.remove(sample_file)

def show_all_file_modes():
    with open(file_modes, "r", encoding='utf-8-sig') as f:
        print(f'File Modes:\n{f.read()}')
        f.close()

def write_to_file():
    with open(sample_file, "w", encoding='utf-8-sig') as f:
        f.write("hello world")
        f.write("\nadios")
        f.close()

def read_entire_file():
    with open(sample_file, "r", encoding='utf-8-sig') as f:
        content = f.read()
        print(f'Full File Content: {content}')
        f.close()

def read_per_line():
    with open(sample_file, "r", encoding='utf-8-sig') as f:
        content = f.readlines()
        print(f'Full File Content as list of lines: {content}')
        f.close()

def iterate_per_line():
    with open(sample_file, "r", encoding='utf-8-sig') as f:
        i: int = 0
        for line in f:
            i += 1
            print(f'Line {i}: {line.strip()}')
            f.close()

def append_to_file():
    with open(sample_file, "a", encoding='utf-8-sig') as f:
        f.write("\nnew world")
        f.close()

def write_binary_file():
    with open(bin_file, "wb") as f:
        f.write(b"\x01\x02\x03")

def read_binary_file():
    with open(bin_file, "rb") as f:
        content = f.read()
        print(f'Full Binary Content: {content}')
        f.close()