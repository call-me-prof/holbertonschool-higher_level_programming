#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these chars: ., ? and :

    Args:
        text: The string to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 1:
            if char == ' ':
                continue
            flag = 0
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n")
            flag = 1
