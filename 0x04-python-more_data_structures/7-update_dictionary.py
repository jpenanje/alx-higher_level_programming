#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k, v in a_dictionary.items():
        if k == key:
            v = value
        else:
            a_dictionary[k] = v
    return a_dictionary
