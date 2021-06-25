'''三角形公式大师-挑战包'''

def hypotenuse(a, b):
    c = (a**2+b**2)**0.5
    c = round(c, 1)
    return c

print(hypotenuse(3, 5))
