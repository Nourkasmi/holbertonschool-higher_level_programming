#!/usr/bin/python3
"""Module to return the JSON representation of an object."""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    :param my_obj: The object to serialize
    :param filename: The name of the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
