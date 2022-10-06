#!/usr/bin/python3
"""
Read a text file
"""


def read_file(filename=""):
    """
    Fuunction that read a file
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
    f.close()
