#!/usr/bin/python3

'''Write a class Rectangle that defines a rectangle.'''


class Rectangle:
    '''Define class Rectangle.'''
    def __init__(self, width=0, height=0):
        '''Create a new rectangle.
        Args:
            width: width of new rectangle.
            height: height/length of new rectangle.
        '''
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

    def area(self):
        '''method that returns rectangle area.'''
        return(self.__width * self.__height)

    def perimeter(self):
        '''method that returns rectangle perimeter.'''
        if self.__width or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Print a rectangle.
        Represents the rectangle with the # character(s).
        """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return (rect)
        for i in range(0, self.__height):
            for j in range(self.__width):
                rect += "#"
            if i is not (self.__height - 1):
                rect += "\n"
        return (rect)