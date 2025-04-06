import math

def f(x):
    return 2 - x - math.exp(-x)

def bisection_method(a, b, tol=1e-8, max_iter=10000):
    if f(a) * f(b) >= 0:
        print("Function does not have different signs at the endpoints.")
        return None

    iter_count = 0
    while (b - a) / 2.0 > tol and iter_count < max_iter:
        c = (a + b) / 2.0
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iter_count += 1

    return (a + b) / 2.0


def secant_method(a, b, tol=1e-8, max_iter=10000):
    iter_count = 0
    while abs(b - a) > tol and iter_count < max_iter:
        if f(b) == f(a):
            print("Division by zero error in Secant method.")
            return None

        c = b - f(b) * (b - a) / (f(b) - f(a))

        a, b = b, c

        iter_count += 1

    return b

a = 0
b = 10
root_bisection = bisection_method(a, b)
root_secant = secant_method(a, b)

print(f"The root is approximately: {root_bisection, root_secant}")
