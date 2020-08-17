from math_series import __version__
from math_series.series import a , fibonacci_fun,fibonacci,lucas,multiple_lucas



def test_one():
    assert a==6

#--------------------fibonacci----------------#
def test_two():
   expected=2
   actual=fibonacci_fun(3)
   assert expected == actual

def test_three():
    expected=5
    actual=fibonacci_fun(5)
    assert expected==actual

def test_many():
    expected=[21,34,55,89,144]
    actual=fibonacci([8,9,10,11,12])
    assert expected==actual

#--------------------LUCAS----------------#
# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123,

def test_lucas_one():
    expected=3
    actual=lucas(2)
    assert expected==actual


def test_lucas_two():
    expected=4
    actual=lucas(3)
    assert expected==actual

def test_lucas_three():
    expected=7
    actual=lucas(4)
    assert expected==actual

def test_lucas_four():
    expected=11
    actual=lucas(5)
    assert expected==actual

def test_many_lucas():
    expected=[18, 29, 47, 76, 123]
    actual=multiple_lucas([6,7,8,9,10])
    assert expected==actual