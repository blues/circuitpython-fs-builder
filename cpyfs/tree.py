# Copyright (c) 2022 Blues Wireless Inc. All Rights Reserved.

"""Writes a filesystem tree to standard output.
"""

import argparse
import fs
import os


def show_tree(fat_fs: str):
    fat_fs_abs = os.path.realpath(fat_fs)
    with fs.open_fs("fat://" + fat_fs_abs) as fat_fs:
        fat_fs.tree()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=str, help="The fat filesystem file to output as a tree.")
    args = parser.parse_args()

    show_tree(args.file)


if __name__ == "__main__":
    main()
