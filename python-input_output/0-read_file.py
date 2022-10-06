#!/usr/bin/python3
def read_file(filename=""):
    """
    Fuunction that read a file 
    """
    with open(filename) as f:
        for line in f:
            print(line)
