
def is_triangle(a,b,c):
    if a + b < c and b + c < a and c + a < b:
        return True
    else:
        return False

print(is_triangle(8,4,5))