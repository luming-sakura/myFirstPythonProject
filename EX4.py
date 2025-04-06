import math
from mpmath import mp

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)

    return root1, root2

a = 1.22
b = 3.34
c = 2.28

roots = solve_quadratic(a, b, c)

if roots:
    print(f"方程的根是: x1 = {roots[0]}, x2 = {roots[1]}")
else:
    print("方程没有实数根")


