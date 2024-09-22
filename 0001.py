import random
import string


def activate_code(num, length=17):
    f = open('Activation_Code.txt', 'w')
    chars = string.digits + string.ascii_letters     # 创建包含所有字符的集合
    for i in range(num):
        code = [random.choice(chars) for _ in range(length)]
        f.write(''.join(code) + '\n')
    f.close()



if __name__ == '__main__':
    activate_code(200, 17)
