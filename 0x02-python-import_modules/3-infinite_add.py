#!/usr/bin/python3

if __name__ == "__main__":
    """print the sum of all arguments"""
    import sys

    args_count = len(sys.argv)
    args_list = sys.argv
    sum = 0

    if args_count == 1:
        print("0")
    elif args_count == 2:
        print("{}".format(args_list[1]))
    else:
        for i in range(args_count):
            sum = int(args_list[i] + sum)
        print("{}".format(sum))
