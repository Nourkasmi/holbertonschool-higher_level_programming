#!/usr/bin/python3
"""Module to return the JSON representation of an object."""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    :param filename: The name of the file to read from
    :return: The deserialized Python object
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
