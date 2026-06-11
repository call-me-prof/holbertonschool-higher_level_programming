#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: The first integer or float.
        b: The second integer or float.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        The addition of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
