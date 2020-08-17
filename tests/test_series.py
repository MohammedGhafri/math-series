from math_series import __version__
from math_series.series import a , fibonacci_fun,fibonacci



def test_one():
    assert a==6


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


# def index_eight():
#     expected=21
#     value=fibonacci_fun(8)
#     assert expected==fibonacci_fun