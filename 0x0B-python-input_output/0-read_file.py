#!/usr/bin/python3

'''Function that reads a text file and prints it to stdout.'''


def read_file(filename=""):
    '''Reads a text file.'''
    with open("", encoding="utf-8") as f:
        read_data = f.read()
