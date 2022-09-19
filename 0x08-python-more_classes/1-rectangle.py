#!/usr/bin/python3

'''Write a class Rectangle that defines a rectangle.'''


class Rectangle:
    '''Define class Rectangle.'''
    def __init__(self, width=0, height=0):
        '''Create a new rectangle.'''
        self.__width = width
        self.__height = height

    @property
    '''get width of new rectangle.'''
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        '''set width of new rectangle'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''retrieve height of new rectangle.'''
        return(self.__height)

    @height.setter
    '''set height of new rectangle.'''
    def width(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
