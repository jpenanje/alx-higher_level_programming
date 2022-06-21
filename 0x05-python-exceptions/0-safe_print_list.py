#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for elements in my_list:
        try:
            print("{}".format(elements), end="")
            i += 1
        except IndexError:
            break
    print()
    return i
