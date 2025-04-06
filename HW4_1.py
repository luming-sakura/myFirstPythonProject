import math


def calculate_roots(b):
    r = math.sqrt(b ** 2 - 4)
    x1 = (b + r) / 2
    x2 = (b - r) / 2

    x2_rationalized = 2 / (b + r)

    true_x2 = 1 / x1
    error_unrationalized = abs((x2 - true_x2) / true_x2)
    error_rationalized = abs((x2_rationalized - true_x2) / true_x2)

    return x1, x2, x2_rationalized, error_unrationalized, error_rationalized

b_values = [100, 1000, 10000, 100000]

print(
    f"{'b':<10} {'x1':<20} {'x2 (未有理化)':<20} {'x2 (有理化)':<20} {'相对误差 (未有理化)':<25} {'相对误差 (有理化)':<25}")
print("-" * 120)

for b in b_values:
    x1, x2, x2_rationalized, error_unrationalized, error_rationalized = calculate_roots(b)
    print(f"{b:<10} {x1:<20} {x2:<20} {x2_rationalized:<20} {error_unrationalized:<25} {error_rationalized:<25}")