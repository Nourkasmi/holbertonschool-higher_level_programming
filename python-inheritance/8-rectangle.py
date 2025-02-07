#!/usr/bin/python3
"""Module 8-rectangle."""


class Rectangle(BaseGeometry):
    """A rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
