#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for elm in range(0, x):
        try:
            print(my_list[elm], end="")
            i += 1
        except (IndexError, ValueError, TypeError):
            break
    print()
    return i
