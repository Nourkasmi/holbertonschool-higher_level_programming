#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
