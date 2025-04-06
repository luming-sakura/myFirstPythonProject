def list_while_func():
    index = 0
    while index < len(mylist):
        element = mylist[index]
        print(f'列表的元素：{element}')
        index += 1
mylist = [[1, 2, 3], [4, 5, 6, 7, 8]]
list_while_func()
print(mylist[1][2])
list1 = list(range(0,5))
print(list1)
print(f"max = {max(list1)},min = {min(list1)}")

def test(x,y):
    return x+y

my_str = 'abcd abdcba acddabba'
count1 = my_str.count('ab')
print(count1)

new_my_str = my_str.strip('ab')
print(new_my_str)

str2 = 'abcdefghijk'
print(str2[::-1])

list2 = list('hello')
print(list2)
list2.insert(1,'o')
print(list2)
delect = list2.pop(2)
print(list2,delect)
set2 = set(list2)
print((set2))
list3 = list(set2)
print(list)

list4 = list('123456789')
print(list4)
list4.extend(list3)
print(list4)


