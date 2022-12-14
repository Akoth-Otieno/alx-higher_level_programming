#!/usr/bin/python3

'''Define a class rectangle that inherits from Base.'''


class Rectangle(__import__('base').Base):
    '''REpresents Rectangle that inherits from Base.'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiate a new rectangle.

        Args:
        width (int): width of new rectangle.
        height (int): height of new rectangle.
        x (int): x-coordinate of new rectangle.
        y (int): y-coordinate of new rectangle.
        id (int): identity of new rectangle.

        The function raises:
        TypeError: If either of width or height is not an int.
        ValueError: If either of width or height <= 0.
        TypeError: If either of x or y is not an int.
        ValueError: If either of x or y < 0
        '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            '''get the width of the rectangle.'''
            return(self.__width)

        @width.setter
        def width(self, value):
            '''sets the width of the rectangle.'''
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            '''gets the height of the rectangle.'''
            return(self.__height)

        @height.setter
        def height(self, value):
            '''sets the height of the ractangle.'''
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            '''sets the x coordinate of the Rectangle.'''
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            '''sets the y coordinate of the Rectangle.'''
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
