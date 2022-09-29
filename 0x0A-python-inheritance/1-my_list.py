#!/usr/bin/python3

'''Define a class list.'''

class MyList(list):
    '''Create an instance of my list.'''
    def print_sorted(self):
        """Sort list in ascending order."""
        print(sorted(self))


