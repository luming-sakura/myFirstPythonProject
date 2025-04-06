n = 500000
total = 0.0
sign = 1

for i in range(n):
    denominator = 2 * i + 1
    total += sign / denominator
    sign *= -1  # 翻转符号

pi_approx = total * 4
print(pi_approx)

n = 500000
total = 0.0
sign = -1 ** (n - 1)

for i in range(n-1, -1, -1):
    denominator = 2 * i + 1
    total += sign / denominator
    sign *= -1

pi_approx = total * 4
print(pi_approx)

'''第二种算法得到的结果相对于第一种更为准确。
这是因为，实际计算中，浮点数的精度有限，当加上很多小数时，如果先加大的项，后面加的小项可能因为精度不够被忽略，而倒序的话，先加小的项，再逐步加大的项，可能更有效保留小数部分的信息。比如，假设i从0到n-1，当i很大时，比如接近500000时，分母是大约1e6的数量级，所以项的大小是大约1e-6，而前面的项比如i=0时，项是1/1=1，i=1时是1/3≈0.333，所以后面的项越来越小。倒序的话，是从i=n-1开始，到i=0，这样最大的项（i=0时的项）会在最后加上。这可能有助于提高精度，因为当累加到后面的大项时，总和已经积累了一些小项的值，这样加大的项时，它们的贡献不会被截断。'''