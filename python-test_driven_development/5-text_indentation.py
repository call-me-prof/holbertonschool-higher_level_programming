#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The string to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # تنظيف الفراغات من البداية والنهاية أولاً
    text = text.strip()
    
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            # لتخطي الفراغات التي تأتي مباشرة بعد علامات الترقيم
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
