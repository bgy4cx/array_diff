from array_diff import *

a = [1, 2, 3, 4]
b = [2, 3]

def test_IsItArray_true():
    assert IsItArray(a) == True

def test_IsItArray_false():
    assert IsItArray(1) == False

