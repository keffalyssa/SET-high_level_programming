#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for c in text:
        if c == ' ':
            if flag == 0:
                continue
            break
        print(c, end="")
        if c in ".?:":
            print("\n")
            flag = 0
        else:
            flag = 1
