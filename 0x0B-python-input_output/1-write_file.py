#!/usr/bin/python3

'''Defines a function that writes to a file.'''


def write_file(filename="", text=""):
    '''writes a string to a text file and returns character count.'''
    with open(filename, mode="w", encoding="utf-8") as f:
        file_lines = 0
        for file_line in f:
            file_line = f.readline()
            file_lines += file_line
    return(file_lines)
