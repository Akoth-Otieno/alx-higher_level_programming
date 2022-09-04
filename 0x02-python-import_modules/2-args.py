#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    arg_count = len(sys.argv) - 1
    args_list = sys.argv

    if arg_count == 1:
        print("{} arguments.".format(arg_count - 1))
    elif arg_count == 2:
        print("{} argument:".format(arg_count - 1))
        print("{}: {}".format(1, args_list[1]))
    else:
        print("{} arguments:".format(arg_count - 1))
        for i in range(1, arg_count):
            print("{}: {}".format(i, args_list[i]))



