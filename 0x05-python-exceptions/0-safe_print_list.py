#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nelements = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            nelements += 1
        except Exception as err:
            break
    print()
    return nelements
