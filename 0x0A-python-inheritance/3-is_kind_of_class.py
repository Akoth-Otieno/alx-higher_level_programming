#!/usr/bin/python3

'''Check if an object is exactly an instance of a given class.'''


def is_kind_of_class(obj, a_class):
    '''determine object type.'''
    if isinstance(obj, a_class):
        return True
    else:
        return False
