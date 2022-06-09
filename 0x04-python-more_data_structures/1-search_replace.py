#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mylist = my_list.copy()
    for i in range(0, len(mylist)):
        if mylist[i] == search:
            mylist[i] = replace
    return mylist
# or return [replace if num == search else num for num in my_list]
