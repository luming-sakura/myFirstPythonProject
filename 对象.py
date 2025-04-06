class Student:
    def p_name(self):
        print(self.name)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("Initialise")


stu1 = Student('aaabbbccc', 18, 'man')
a = '我也不知道写什么'
b = sorted(a)
print(b)
