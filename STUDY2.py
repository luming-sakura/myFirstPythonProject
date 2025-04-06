#索引和切片
#适用于字符串
UID = '214236889'
print(UID[::-1])
print(UID[:5:2])
print(UID[::])

print(UID[5],UID[3])
number1 = UID[5]
number2 = UID[3]
print(number1 + number2)
number1 = int(number1)
number2 = int(number2)
print(number1 + number2)
#结果:6 2
#    62
#    8



#[初始位置：终止位置：步长]
#步长：间隔的距离，从初始位置开始
#终止位置不计入
#[::-1]倒序



#数字类型：列表(list)
#使用方法：用[]，内部用","隔离开
a1 = ['one last kiss','SAYONARA',2351,555,5622]
print(type(a1))
a1[0] = 'I really want stay in your house'
#结果为['I really want stay in your house', 'SAYONARA', 2351, 555, 5622]
print(a1)
a1[2:] = [5555555,878]
print(a1)
#结果为['I really want stay in your house', 'SAYONARA', 5555555, 878]
#列表修改时，如果对应位置没有元素，则会直接删除
#列表可以进行修改

#访问list中的值
#使用[]截取字符

print(type(a1[1]))
#结果：str
print('a1[1]:'+a1[1])
print(type(a1[3]))
#结果：int
#对于列表里每一项的数字类型，取决于此项本身
print(a1[1:])








#in 判断字符串内 是否含有其他字符串，输出结果为bool
#len()返回字符串的长度，输出结果为int
"""a2 = input('give me three different number'),input(),input()
result1 = '10' in a2
if result1 == 1:
    print('win')
else:
    print('lose')
"""



a3 = '1000','100000'
print(len(a3))
#结果为2

a4 = '10000'
print(len(a4))
print(type(len(a4)))
#结果为5，类型为int


a5 = '214236889'
print(max(a5))
print(min(a5))
a6 = '1000','545155','2'
print(type(max(a6)))
#结果为str
print(max(a6) + ',' + min(a6))
#max(),min()均只对字符串生效

# .index 查询下标
# 重复元素，得到最小下标
list1 = [1,1,5,3,6,88]
index1 = list1.index(1)
print(index1)

# .insert(下标，元素) 插入元素
# .append(元素)追加元素
# .extend(其他数据容器)多个追加











