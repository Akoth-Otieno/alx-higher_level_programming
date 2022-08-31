#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''Adds all the unique elements of a list.'''
    result = 0
    for i in set(my_list):
        result = result + i
    return (result)

