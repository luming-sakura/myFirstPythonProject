import math


# 定义函数 f(x)
def f(x):
    return 4 * math.cos(x) - math.exp(x)


def f_prime(x):
    return -4 * math.sin(x) - math.exp(x)

def full_nr_bisection(f, f_prime, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        print("错误：区间[a, b]上没有根")
        return None

    iter_count = 0
    while iter_count < max_iter:
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol:
            print(f"找到根 c = {c}，迭代次数: {iter_count}")
            return c
        if f(a) * fc < 0:
            b = c
        else:
            a = c

        try:
            c_newton = c - f(c) / f_prime(c)
            if abs(f(c_newton)) < abs(f(c)):
                c = c_newton
        except ZeroDivisionError:
            pass

        iter_count += 1

    print("达到了最大迭代次数")
    return (a + b) / 2


a = 0
b = 2

root = full_nr_bisection(f, f_prime, a, b)
if root is not None:
    print(f"根的近似值为: {root}")