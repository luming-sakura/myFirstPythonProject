dict1 = {
    'a': {'工资': 5000, '部门': '科技部', '级别': 1},
    'b': {'工资': 4000, '部门': '技术部', '级别': 2},
    'c': {'工资': 5000, '部门': '科技部', '级别': 3},
    'd': {'工资': 3000, '部门': '营业部', '级别': 1}
}
for name in dict1:
    if dict1[name]['级别'] == 1:
        employ_dict = dict1[name]
        employ_dict['级别'] += 1
        employ_dict['工资'] += 1000
        dict1[name] = employ_dict
print(dict1)

ID_dict = {'1': 500000000, '2': 40000000, '3': 300000000}
ID = input()
money = ID_dict[ID]
print(money)