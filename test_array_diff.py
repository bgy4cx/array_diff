from array_diff import *

def test_IsItArray_true():
    assert IsItArray([1, 2, 3, 4]) == True

def test_IsItArray_false():
    assert IsItArray(1) == False

def test_array_diff_1():
    assert array_diff([1, 2, 3, 4], [2, 3]) == [1, 4]

def test_array_diff_2():
    assert array_diff([2, 3], [1, 2, 3, 4]) == []

