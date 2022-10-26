#!/usr/bin/python3
class Mylist(list):
    """
    class that inherits from class list

    Args:
        list: parent class

    """


    def print_sorted(self):
        """Method printing a sorted list"""
        sorted_list = self.copy()
        print(sorted_list.sort())
