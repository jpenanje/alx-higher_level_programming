#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k, v in a_dictionary.items():
        if k == key:
            key = value
        else:
            a_dictionary.update({key:value})
    return a_dictionary
