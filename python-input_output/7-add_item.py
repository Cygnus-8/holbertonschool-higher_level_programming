#!/usr/bin/python3

"""
Os module to check if a file exist
Sys module to retrieve argument
"""
import os
import sys

"""
Save to Json file method
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""
load from json file method
"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if not os.path.exists("add_item.json"):
    save_to_json_file(sys.argv[1:], "add_item.json")
else:
    str = load_from_json_file("add_item.json")
    str = str + sys.argv[1:]
    save_to_json_file(str, "add_item.json")
