#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    args_count = len(sys.argv) - 1

    if args_count <= 1:
        print("0 arguments.")
    else:
        if args_count == 2:
            print("{:d} argument:".format(args_count))

        else:
            print("{:d} arguments:".format(args_count))
        for i in range(1, args_count):
            print("{:d}: {}".format(i, sys.argv[i]))
