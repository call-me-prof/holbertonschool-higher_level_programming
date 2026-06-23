#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list with custom printing behavior."""

    def print_sorted(self):
        """Prints the list in sorted ascending order."""
        print(sorted(self))
