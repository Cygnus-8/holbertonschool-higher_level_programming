#!/usr/bin/python3

"""
Json string module
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an object from a text file
    using a JSON String
    """
    with open(filename, "r") as f:
        str = json.load(f)
    f.close()
    return (str)
