#!/usr/bin/python3
"""Module 8-rectangle.

This module defines a Rectangle class that inherits from BaseGeometry.
It represents a rectangle with width and height attributes validated as
positive integers.
"""


class Rectangle(BaseGeometry):
    """A Rectangle class inheriting from BaseGeometry to model a rectangle."""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance with validated dimensions.

        Args:
            width (int): The rectangle's width. Must be a positive integer.
            height (int): The rectangle's height. Must be a positive integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
