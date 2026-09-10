from operator import truediv


def pythagorean_triples( a, b, c):
  if  a**2+b**2==c**2:
    return True
  elif a**2+b**2>c**2:
    return False
  else:
    return False
    print(pythagorean_triples(3,4,7))


