#!/usr/bin/python3
"""
Module defining the CountedIterator class.
Keeps track of the number of items that have been iterated over.
"""


class CountedIterator:
    """An iterator wrapper that maintains a counter of iterated items."""

    def __init__(self, iterable):
        """Initialize the iterator object and the counter."""
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Fetch the next item and increment the counter.

        Raises StopIteration if there are no items left.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
