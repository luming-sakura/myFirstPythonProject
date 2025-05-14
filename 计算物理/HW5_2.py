import math

def f(x, h):
    # x * tan(x) - sqrt(h^2 - x^2)
    return x * math.tan(x) - math.sqrt(max(h*h - x*x, 0.0))

def g(x, h):
    # x * cot(x) + sqrt(h^2 - x^2)
    t = math.tan(x)
    return x * (1.0/t if t != 0 else float('inf')) + math.sqrt(max(h*h - x*x, 0.0))

def bisection(func, h, a, b, tol=1e-6, max_iter=50):
    fa, fb = func(a, h), func(b, h)
    if fa * fb > 0:
        return None
    for _ in range(max_iter):
        m = 0.5 * (a + b)
        fm = func(m, h)
        if abs(fm) < tol or (b - a)/2 < tol:
            return m

        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return 0.5 * (a + b)


def find_roots(func, h, steps=200):
    roots = []
    a, b = -h, -h + (2*h)/steps
    fa = func(a, h)
    for i in range(1, steps + 1):
        b = -h + (2*h)*i/steps
        fb = func(b, h)
        if fa * fb <= 0:
            root = bisection(func, h, a, b)
            if root is not None:
                roots.append(root)
        a, fa = b, fb
    return roots

# Example usage
def main():
    h_values = [0.2, 0.5, 1.0, 2.0]
    for h in h_values:
        roots_f = find_roots(f, h)
        roots_g = find_roots(g, h)
        print(f"h = {h}")
        print("  Roots of f(x):", [round(r, 6) for r in roots_f])
        print("  Roots of g(x):", [round(r, 6) for r in roots_g])

if __name__ == '__main__':
    main()
