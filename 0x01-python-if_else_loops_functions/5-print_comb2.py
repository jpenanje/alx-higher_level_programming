#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        print("{}{}".format(number // 10, number % 10), end=", ")
    else:
        print("{}".format(number))
