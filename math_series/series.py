a =6

# task 1
def fibonacci_fun(index):
    """
    Return fibonacci series's value at index n i.e F(index).
    
    Arguments:
    index {integer} -- index of in series

    Output:
    fibonacci(index) {Integer} --the estimated value for index
    """
    if index < 0:
        pass
    elif index == 0:
        return 0
    elif index == 1:
        return 1
    return fibonacci_fun(index-1) + fibonacci_fun(index-2)

    
# CAll fibonacci for index n
def fibonacci(arr):
    return [fibonacci_fun(i) for i in arr ]

# task 2

def lucas(num):
    """
    Return lucas series's value at index n. i.e F(index).
    
    Arguments:
    index {integer} -- index of in series

    Output:
    lucas(index) {Integer} --the estimated value for index
    """
    if num<0:
        pass
    elif num==0:
        return 2
    elif num ==1 :
        return 1
    return lucas ( num - 1 ) + lucas ( num - 2 )

def multiple_lucas(arr):
    return [lucas (i) for i in arr]


# task 3
def sum_series(num,a=0,b=1):
    """
    Return a value at index n. i.e sum_seriesF(index).
    This value is changable upon  a,b indices which are an optional  user's input.
    
    
    Arguments:
    num {integer} -- index of in series
    a   {integer} -- value of first  base  in series.By default its equal to 0 as Fibonacci series
    b   {integer} -- value of second base  in series.By default its equal to 1 as Fibonacci series

    Output:
    sum_series {integer} --
                            If a=0 and b=1; then sum_series will be equal to fibonacci_fun function
                            If a=2 and b=1; then sum_series will be equal to lucas function
                            Other wise will give different values
    """
    # if num<0:
    #     pass
    # # if num ==0:
    # #     return a
    # # elif num == 1:
    # #     return b
    # if a==0 :
    #     return fibonacci_fun(num)
    # elif a==2 :
    #     return lucas(num)
    
    # else:
    if num ==0:
        return a
    elif num==1:
        return b
    return sum_series (num - 1,a,b) + sum_series(num - 2,a,b)

# for i in range(0,10):
#     print(sum_series(i,0,0))

print(sum_series(0,3,1))