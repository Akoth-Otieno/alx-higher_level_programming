#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Define size as private instance attribute"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
