#!/usr/bin/python3
"""Geometry class."""


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
