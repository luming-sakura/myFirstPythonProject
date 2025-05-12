import cmath

def solve_cubic(a, b, c, d):
    if a != 1:
        b /= a
        c /= a
        d /= a

    p = c - b**2 / 3
    q = (2 * b**3) / 27 - (b * c) / 3 + d
    delta = (q / 2)**2 + (p / 3)**3

    if delta > 0:
        # 一个实根，两个共轭复根
        u = (-q/2 + cmath.sqrt(delta))**(1/3)
        v = (-q/2 - cmath.sqrt(delta))**(1/3)
        root1 = u + v - b/3
        root2 = -(u+v)/2 - b/3 + (u-v)*cmath.sqrt(3)*1j/2
        root3 = -(u+v)/2 - b/3 - (u-v)*cmath.sqrt(3)*1j/2
    elif delta == 0:
        # 三个实根，至少两个相等
        u = (-q/2)**(1/3)
        root1 = 2*u - b/3
        root2 = root3 = -u - b/3
    else:
        # 三个不相等实根
        rho = cmath.sqrt(-(p**3)/27)
        theta = cmath.acos(-q/(2*rho))
        rho = (-p/3)**0.5
        root1 = 2 * rho * cmath.cos(theta/3) - b/3
        root2 = 2 * rho * cmath.cos((theta + 2*cmath.pi)/3) - b/3
        root3 = 2 * rho * cmath.cos((theta + 4*cmath.pi)/3) - b/3

    return root1, root2, root3

a = 1
b = -705
c = 1533.54
d = -10082.44

roots = solve_cubic(a, b, c, d)
print("三次方程的根为：")
for idx, root in enumerate(roots, start=1):
    if abs(root.imag) < 1e-8:
        root = root.real
    print(f"根 {idx}: {root}")
