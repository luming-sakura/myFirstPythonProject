def print_file_info(file_name):
    """
    将指定路径的文件输出到控制台
    :param file_name: 即将读取的文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UFT-8")
        content = f.read()
        print('文件的全部内容如下：')
        print(content)
    except Exception as e:
        print('ERROR', e)
    finally:
        if f:
            f.close()



def append_to_file(file_name, data):
    """
    追加数据到指定文件
    :param file_name:文件目录
    :param data: 追加内容
    :return:
    """
    f = open(file_name, 'a', encoding="UTF-8")
    f.write(data)
    f.write('\n')
    f.close()




if __name__ == '__main__':
    print_file_info("D:/bill.txt")
    append_to_file('D:/bill.txt', "黑马程序员")

