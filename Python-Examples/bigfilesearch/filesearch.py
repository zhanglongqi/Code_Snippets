#!/usr/bin/env python
"""
A script that reads a very large text file,
outputs the length of char strings separated
by "$" sign.

This script assumes the file is line-based.
"""

from utils import get_filename, calculate_len_of_strs

if __name__ == '__main__':
    # GRAB FILENAME
    filename = get_filename()

    # As the text file will be larger than the virtual memory, mmap is not
    # feasible here.
    # Best way to deal with the big files is using "with open" methodology.
    with open(filename) as bigfile:
        for line in bigfile:
            # It trims the trailing whitespaces and splits the line
            # with the seperator '$'
            print calculate_len_of_strs(line.rstrip().split('$'))