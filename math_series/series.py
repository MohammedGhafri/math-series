a =6


def fibonacci_fun(index):
    if index < 0:
        pass
    elif index == 0:
        return 0
    elif index == 1:
        return 1
    return fibonacci_fun(index-1) + fibonacci_fun(index-2)

    

def fibonacci(arr):
    return [fibonacci_fun(i) for i in arr ]


# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123,
def lucas(num):
    if num<0:
        pass
    elif num==0:
        return 2
    elif num ==1 :
        return 1
    return lucas ( num - 1 ) + lucas ( num - 2 )

def multiple_lucas(arr):
    return [lucas (i) for i in arr]