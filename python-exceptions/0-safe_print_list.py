#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    start = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            start += 1
        except IndexError:
            break
    print("")
<<<<<<< HEAD
    return (start)
=======
    return (start)
>>>>>>> a65375233e6d363a9f20ef59126db1c52e3cc10e
