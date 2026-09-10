def trailing_zeros(n):
    if n % 10 == 0:
        return 1 + (trailing_zeros(n // 10))
    else:
        return 0
""" 
n --> # of trailing zeros in n 
trailing_zeros(n) takes in a value n and if the remainder of n once divided by 10 is eqaul to 0 it returns the number of trailing zeros otherwise it returns 0 
>>>print(trailing_zeros(4000))
3
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def trailing_zeros_in_factorial(n):
   return trailing_zeros(factorial(n))

"""" n --> # of trailing zeros in n! 
trailing_zeros_in_factorial(n) takes in value n if the remainder of n after being divided by 10 is 0, n is eqaul to n/10 and returns n x the function calling itself n -1 
>>>print(trailing_zeros_in_factorial(20))
4
>>>print(trailing_zeros_in_factorial(30))
7
"""








