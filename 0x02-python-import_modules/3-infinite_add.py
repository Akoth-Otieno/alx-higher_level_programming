#!/usr/bin/python3

if __name__ == "__main__":
    """print the sum of all arguments"""
    import sys

    args_count = len(sys.argv)
    sum = 0
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
