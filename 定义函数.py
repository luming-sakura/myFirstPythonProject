# 定义函数的格式：def
name = None
ID_dict = {'1': 500000000, '2': 40000000, '3': 300000000}
i = 1
def input_name():
    global name
    name = input('ID:')
input_name()
while i == 1:
    if name in ID_dict:
        money = ID_dict[name]
        i += 1
    else:
        print('we did not find your account, please tyr again.')
        input_name()

requirement = None
def query(bool):
    if bool:
        print('--------------balance enquiry--------------')
    print(f'Good morning,Mr.{name},now your account have {money}.')
    print('What do you what to do next?')
    initialization(False)

def saving():
    global money
    saving_num = int(input('now input the amount of deposit'))
    money += saving_num
    print(f'successfully!You have saved {saving_num}.')
    query(False)

def get_money():
    global money
    out_num = int(input("how many do you want to put out"))
    money -= out_num
    if money >= 0:
        print(f'Successfully!Now you have put out {out_num}.')
    else:
        print('Failed!You don\'t have enough money.')
        initialization(False)
    query(False)

def task():
    while requirement is not None:
        if requirement == '1':
            query(1)
            break
        elif requirement == '3':
            saving()
            break
        elif requirement == '2':
            get_money()
            break
        elif requirement == '4':
            print('Thank you for your using')
            break
        else:
            print('wrong number,please try again')
            initialization(False)

def initialization(bool2):
    global requirement
    if bool2:
        print(f'welcome!Mr.{name}.Now you can input the number to reach you requirement.')
    print('if you want know your remaining sum,please input 1')
    print('if you want draw money,please input 2')
    print('if you want save money,please input 3')
    print('exit,please input 4')
    requirement = input()
    task()

initialization(1)






