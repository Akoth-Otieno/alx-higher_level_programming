#!/usr/bin/python3

'''check if object is an instance of a class.'''


def inherits_from(obj, a_class):
    '''check class inheritance.'''
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
