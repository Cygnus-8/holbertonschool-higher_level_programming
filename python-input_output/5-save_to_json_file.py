#!/usr/bin/python3

"""
Json string module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file
    using a JSON representation
    """
    str = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(str)
    f.close()
