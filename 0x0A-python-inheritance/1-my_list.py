#!/usr/bin/python3

'''Define a class list.'''


class MyList(list):
    """ instantiate MyList"""
    def print_sorted(self):
        """sort my list"""
        print(sorted(self))
