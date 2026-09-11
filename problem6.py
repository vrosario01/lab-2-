def successor(x):
    return x + 1

def add_without_add(a, b):
    result = a
    for _ in range(b):
        result = successor(result)
    return result

""" number, number -> number
add_without_add takes in two numbers and returns their sum.
>>> add_without_add(1, 4)
5
>>> add_without_add(6, 4)
10 """