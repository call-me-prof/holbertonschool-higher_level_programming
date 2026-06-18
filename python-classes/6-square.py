#!/usr/bin/python3
"""Defines a Square class with custom string representation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the size."""
        return self.__width if hasattr(self, '__width') else self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with #."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the printable representation of the Square."""
        if self.__size == 0:
            return ""

        lines = ["\n" * self.__position[1]]
        for i in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
            if i != self.__size - 1:
                lines.append("\n")
        return "".join(lines)
