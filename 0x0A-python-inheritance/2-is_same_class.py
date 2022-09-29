#!/usr/bin/python3

'''check if an object is an instance of specified class.'''


def is_same_class(obj, a_class):
    ''' returns True.'''
    if type(obj) == a_class:
        return True
    return False
