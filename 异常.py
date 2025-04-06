def func1():
    print('func1 start')
    num = 1 / 0
    print('func1 ending')

def func2():
    print('func2 start')
    func1()
    print('func2 ending')

def main():
    try:
       func2()
    except Exception as e:
        print(e)

main()