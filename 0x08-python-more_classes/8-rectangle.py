#!/usr/bin/python3
"""8-rectangle, built for Holberton Python project 0x08 task 8.
"""


class Rectangle:
    """Class for printing or computation of dimensions of a rectangle.

    Takes in args for width and height of a rectangle, and contains methods
    for calculation of the area or perimeter. __str__, __repr__, and __del__
    fuctionality defined below.

    Attributes:
        number_of_instances (int): counter incrementing for every
            instantiation, and decrementing for every instance deletion.
        print_symbol (str): single character to be used in assembling string
            representation of rectangle

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Increments `number_of_instances` and calls setters for `__width`
        and `__height`.

        Args:
            width (int): horizontal dimension of rectangle, defaults to 0
            height (int): vertical dimension of rectangle, defaults to 0
