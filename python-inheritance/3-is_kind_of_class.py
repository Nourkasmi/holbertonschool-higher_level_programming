#!/usr/bin/python3
"""
Module that defines the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or an instance of a class
    that inherited from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance, False otherwise.
    """
    return isinstance(obj, a_class)
