#!/usr/bin/python3

'''Create a class Square that inherits from BaseGeometry.'''


class Square(__import__('9-rectangle').Rectangle):
    """ class Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
