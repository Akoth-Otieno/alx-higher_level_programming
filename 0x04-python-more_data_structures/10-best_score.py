#!/usr/bin/python3

def best_score(a_dictionary):
    '''returns the key with the biggest integer value.'''
    if a_dictionary is None or len(a_dictionary) <= 0:
        return (None)
    ret = list(a_dictionary.keys())[0]
    best = a_dictionary[ret]
    for key, value in a_dictionary.items():
        if value > best:
            best = value
            ret = key
    return (ret)
