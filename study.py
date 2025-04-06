"""
int:整数
float:浮点数
complex:复数
str:字符串
"""


"""
a1='5'
print(type(a1))
b1='6'
print(a1+b1)
print(type(a1+b1))
a2=int(a1)
print(type(a2))
"""

a1 = """11
22
333
444
"""
a2 = """11
654
6555332
5555
"""

"""
print(a1+a2)
print(type(a1+a2))
"""
print('name = %c,age = %d' % (7,20))
print('pai = %.5f' % 3.1415926)
a3=-745
a3=str(a3)
print("hjshfhsjk "+a3+" fjasfjafd")
print("hasjfhjh %s nsfkj" % 5154561)

#对表达式格式化
print(f"resule is {1*6}")
print('“字符串”在python中的格式 : %s' % type("字符串"))

#'.format' 格式化
s1 = 'the song I\'m listenning now is {},and the next song is {}' .format('amnesia','金木犀')
print(s1)



#转义字符 '\'
print(r'C:\Program Files\Intel')
print('C:\\Program Files\\Intel')

"""
\r 回车符
\n 换行符
\t 制表符
\b 退格符
\f 换页符
"""

#索引和切片
UID = 214236889
print(UID[::])


#运算符
#c+=a 等效于 c=c+a
c1 = 215
a9 = 11
c1+=a9
print(c1)
c1=c1+a9
print(c1)

result = 10>5
print(result)
print(type(result))
result = str(result)
print(type(result))
print(f"The rerult of '10>5' is:{10>5}")
print("10>5的结果是：" + result)

#自由发挥
first = input('give me a nember')
print(type(first))
first = int(first)
second  = 100
second *= first
print('you will get a new nember,and it is: %d' % second)
third = input('then give me another nember')
third = int(third)
if second > third :
    print('win')
elif second == third:
    print('stop')

else:
    print('lose')

#something about 'input()'
'''
First:the type of anything you input is 'str'
So you should translate it into 'int'
'''


