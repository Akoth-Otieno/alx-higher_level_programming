#!/usr/bin/python3

'''Write a class MyInt that inherints from int.'''


class MyInt(int):
    '''class MyInt.'''
    def __init__(self, integer):
        '''Instantiate MyInt and invert operators.'''
        self.integer = integer

    def __eq__(self, rebel):
        return self.integer != rebel

    def __ne__(self, rebel):
        return self.integer == rebel
