#!/usr/bin/python3
"""add item"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.
    """
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
