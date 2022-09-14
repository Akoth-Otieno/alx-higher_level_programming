#!/usr/bin/python3

"""Define a class square."""


class Square:
    """Initialize size as private instance attribute"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """Define public instance method that returns area"""
        return (self.__size * self.__size)
