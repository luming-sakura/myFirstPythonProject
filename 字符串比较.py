print(f'ad > d 的结果是:{"ad" > "d"}')
x = int(input())
y = int(input())
def test_info(compute):
    result = compute(x, y)
    print(result)
def compute(x, y):
    return x + y
test_info(compute)

