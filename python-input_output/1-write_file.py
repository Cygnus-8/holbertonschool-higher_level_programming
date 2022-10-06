#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename='', text=''):
    """
    Functions that writes a string and return
    the number of character written
    """
    with open(filename, "w") as f:
        f.write(text)
    f.close()
    return (len(text))
