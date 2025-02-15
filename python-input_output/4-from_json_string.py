#!/usr/bin/python3
"""Module to return the JSON representation of an object."""


import json


def from_json_string(my_str):
    """
    Returns a Python data structure from a JSON string.
    :param my_str: JSON string
    :return: Corresponding Python object
    """
    return json.loads(my_str)
