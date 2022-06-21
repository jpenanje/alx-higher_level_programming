#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for elm in range(x):
        try:
            print(my_list[elm], end="")
            i += 1
        except Exception as err:
            break
    print('')
    return i
