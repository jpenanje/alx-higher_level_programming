#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{}".format(value))
        return True
    except Exception as err:
        return False
