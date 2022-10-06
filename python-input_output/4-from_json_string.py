#!/usr/bin/python3

"""
Json string module
"""
import json


def from_json_string(my_str):
    """
    Function that returns the Python representation
    of a Json String
    """
    return(json.loads(my_str))
