def __str__(self):
        """Return the printable representation of the Rectangle with #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string representation to recreate the instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
