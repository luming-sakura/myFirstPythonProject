import mpmath

def compute_pi(digits):
    # 设置计算精度（额外增加2位以避免舍入误差）
    mpmath.mp.dps = digits + 2
    # 使用mpmath内置的Chudnovsky算法计算π
    pi = mpmath.mp.pi()
    # 将结果转换为字符串，并截取小数点后的指定位数
    return str(pi)[2:2 + digits]

# 示例：计算小数点后100000位
pi_digits = compute_pi(1000000)

# 输出前100位作为验证
print("π的前1000000位：")
print(pi_digits[:1000000])