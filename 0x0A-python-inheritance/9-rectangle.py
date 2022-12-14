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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        '''Return Rectangle using print() and str().'''
        return(f"[Rectangle] {self.__width}/{self.__height}")
