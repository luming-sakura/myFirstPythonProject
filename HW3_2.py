from decimal import Decimal, getcontext

# 设置计算精度为35位（确保第30位精确）
getcontext().prec = 35

def arctan(x, precision):
    result = Decimal(0.0)
    term = x
    k = 1
    sign = 1
    while abs(term) > precision:
        result += sign * term
        k += 2
        term = term * x * x / k
        sign *= -1
    return result

term1 = 4 * arctan(Decimal(1) / Decimal(5), Decimal(1e-35))
term2 = arctan(Decimal(1) / Decimal(239), Decimal(1e-35))

pi = (term1 - term2) * 4

pi_str = format(pi, '.35f')
final_result = pi_str[:30]

print(f"π：{final_result}")