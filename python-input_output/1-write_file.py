#!/usr/bin/python3
"""Module to write a string to a UTF-8 text file."""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns
    the number of characters.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
