#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """EXecutes a function.

    Args:
        fct: pointer to function to call and execute
        *args: arguments to the function

    Returns:
        the results of the function call
        OR
        None - in case an error occurs
    """
    try:
        result = fct(*args)
        return (result)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
