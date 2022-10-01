#!/usr/bin/python3

'''Defines a function that writes to a file.'''


def write_file(filename="", text=""):
    '''writes a string to a text file and returns character count.'''
    file_lines = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        for file_line in f:
            file_line += 1
    print(file_lines)
