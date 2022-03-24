# Copyright (c) 2022 Blues Wireless Inc. All Rights Reserved.

"""This script produces a file containing a FAT filesystem from a local directory. The file produced is
suitable for flashing to the filesystem storage area of a device running CircuitPython.
"""

import argparse
import fs
import os
from pyfatfs import PyFat


def trim_file(filename: str, trim_value: int, verbose: bool):
    with open(filename, "rb+") as read_file:
        contents = bytearray(read_file.read())

        original_size = len(contents)
        size = original_size
        while size > 0 and contents[size - 1] == trim_value:
            size -= 1

        if size != original_size:
            if verbose:
                print(f"Truncating file {filename} from {original_size} to {size} bytes")
            read_file.truncate(size)


def mkfs(filename: str):
    fat = PyFat.PyFat()
    fat.mkfs(filename, fat_type=PyFat.PyFat.FAT_TYPE_FAT12, label="CIRCUITPY  ")
    fat.close()


def remove_all(output_fs):
    output_fs.removetree("/")


def build_fatfs(seed_file: str, input_path: str, output_file: str, verbose: bool):
    """Constructs a FAT filesystem in a file.

    seed_file:      The file used to seed the filesystem. Relative to this script file.
    input_path:     The directory containing the files to copy to the FAT filesystem. Relative to cwd.
    output_file:    The file
    """
    current_script = os.path.realpath(__file__)
    script_dir = os.path.dirname(current_script)
    output_file_abs = os.path.realpath(output_file)
    seed_file_abs = os.path.join(script_dir, seed_file)

    # open_fs defines the root of the filesystem. In order to allow the files to be in arbitrary locations, we
    # must use absolute paths and open from the root
    with fs.open_fs("/") as seed:
        seed.copy(seed_file_abs, output_file_abs, True)

    # open the input and output filesystems
    with fs.open_fs(input_path) as input_fs:
        with fs.open_fs("fat://" + output_file_abs, writeable=True, create=True) as output_fs:
            remove_all(output_fs)
            fs.copy.copy_fs(input_fs, output_fs, preserve_time=True)

    trim_file(output_file_abs, 0xFF, verbose)

    if verbose:
        show_tree(output_file_abs)

    verify_fs(output_file_abs, input_path)


def show_tree(fat_fs: str):
    fat_fs_abs = os.path.realpath(fat_fs)
    with fs.open_fs("fat://" + fat_fs_abs) as fat_fs:
        fat_fs.tree()


def verify_fs(fat_fs_abs: str, local_path: str):
    with fs.open_fs(local_path) as input_fs:
        with fs.open_fs("fat://" + fat_fs_abs) as fat_fs:
            input_count = input_fs.glob('**/*.*').count()
            fat_count = fat_fs.glob('**/*.*').count()
            if input_count != fat_count:
                raise IOError(f"Internal Error: Filesystem counts do not match. {input_count} != {fat_count}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")
    parser.add_argument("input_dir", type=str, help="The local directory to convert to a filesystem.")
    parser.add_argument("output_file", type=str, help="The output file where the filesystem is written.")
    args = parser.parse_args()

    fat_seed_file = "./seed.bin"
    build_fatfs(fat_seed_file, args.input_dir, args.output_file, verbose=args.verbose)


if __name__ == "__main__":
    main()
