#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argcount = len(sys.argv) - 1
    if argcount == 0:
        print("0 arguments.")
    else:
        if argcount == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(argcount))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
