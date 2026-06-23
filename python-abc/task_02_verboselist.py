#!/usr/bin/python3
"""
Module defining a VerboseList class that extends the built-in list.
Prints notification messages for append, extend, remove, and pop operations.
"""


class VerboseList(list):
    """A custom list that logs messages upon modifications."""

    def append(self, item):
        """Add an item to the end of the list and print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """Extend the list by appending all items from the iterable."""
        items_count = len(x)
        super().extend(x)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        """Remove the first item from the list whose value is equal to item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return the item at the given index (default last)."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
