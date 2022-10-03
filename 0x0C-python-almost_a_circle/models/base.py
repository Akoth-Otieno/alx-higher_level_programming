#!/usr/bin/python3

'''Define a class called Base'''


Class Base:
    '''The base class.'''
     __nb_instances = 0

    def __init__(self, id=None):
        '''class constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
