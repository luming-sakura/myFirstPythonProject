# 字符串工具
def str_reserve(s):
    """
    将字符串进行反转
    :param s: 传入的字符串
    :return: 反转后的字符串
    """
    return s[::-1]

def sub_str(s,x,y):
    """
    指定字符串的切片
    :param s: 被执行的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 得到的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reserve('黑马程序员'))
    print(sub_str('黑马程序员', 1, 3))


