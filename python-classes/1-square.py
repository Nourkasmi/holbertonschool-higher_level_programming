#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """A class that defines a square with a private size attribute."""
    def __init__(self, size):
        """
        Initializes a new Square.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
