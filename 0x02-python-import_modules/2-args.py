#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    arg_count = len(sys.argv) - 1
    args_list = sys.argv

    if arg_count == 0:
        print("0 arguments.")

    elif arg_count == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(count))

    for i in range(arg_count):
        print("{}: {}".format(i + 1, args_list[i + 1]))



