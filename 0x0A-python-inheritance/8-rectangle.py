#!/usr/bin/python3

'''Create a class Rectangle that inherits from BaseGeometry.'''


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    '''Rectangle is a subclass of BaseGeometry.'''
    def __init__(self, width, height):
        '''Instantiate REctangle.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
