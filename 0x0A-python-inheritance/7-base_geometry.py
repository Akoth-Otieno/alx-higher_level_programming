#!/usr/bin/python3

'''Write a class base geometry.'''


class BaseGeometry:
    '''Define class base geometry.'''
    def __init__(self):
        '''Instantiate class.'''
        pass

    def area(self):
        '''public instance method that raises an Exception.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''public instance method that validates a value.'''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
