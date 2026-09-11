
def sum_id(n):
    """ number -> factorial(number) or sum
    sum_id(n) takes in a positive number n and returns the sum from 1 to n: 1+2+3+...+n :
    >>>print(sum_id(2))
    3
    >>>print(sum_id(3))
    6"""
    if n == 1:
        return 1
    else:
        return n + sum_id(n-1)



def sum_squares(n):
    """ n --> n**n + (n-1)
    sum_squares takes in a positive number n and if n = 1 returns 1 otherwise it returns the sum of the square of the numbers from 1 to n: 1^2+2^2+3^2+...+n^2.
    >>>print(sum_squares(2))
    5
    >>>print(sum_squares(3))
    14"""

    if n == 1:
        return 1
    else:
        return n*n + sum_squares(n-1)


def f(x):
    return x
def sum(n, f):
    """number, function -> number
      sum(n, f) takes in a number n and a function f and returns the sum of f applied to the numbers from 1 to n.
     >>> print(sum(4, f))
     10
     >>> print(sum(3, f))
     6"""
    if n == 0:
        return 0
    return f(n) + sum(n - 1, f)


def combine_sequence(n, f, combine=lambda a, b: a + b):
    """ number, function, function -> number
    combine_sequence  takes in a number n and two functions, one called combine and one called f, where f is the function as before and combine now controls the manner in which terms are combined.
    If not otherwise specified, combine_sequence sums the values of the function applied to the numbers from 1 to n.
    >>> print(combine_sequence(3, f))
    6
    >>> print(combine_sequence(4, f))
    10"""
if n == 1:

    return f(1)
    return combine(f(n), combine_sequence(n - 1, f, combine))
