# This function verify the variable and the result is true in case of an array. 
from itertools import cycle


def IsItArray(a):
    return isinstance(a, list)

def array_diff(a, b):
    for x in b:
        i = 0
        while i < len(a):
            if a[i] == x:
                a.pop(i)
            else:
                i+=1
    return a