#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum as an integer.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number, defaults to 98.

    Returns:
    int: The sum of a and b, casted to an integer.

    Raises:
    TypeError: If either a or b is not an integer or a float.
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
