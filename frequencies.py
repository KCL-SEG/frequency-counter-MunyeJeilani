"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    for an_element in items:
        key = str(an_element)
        frequencies[key] = frequencies.get(key, 0) + 1
    return frequencies
