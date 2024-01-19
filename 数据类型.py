# 列表和元组的区别
# 列表可变，元组不可变

list1 = ['a', 'b', 'c', 'd']

# print(len(list1))

tuple1 = (1, 2, 3, 4, 5)

# print(len(tuple1))

# dict集合
dict1 = {'lee': 75, 'wang': 60}

# 判断集合内是否存在某属性
# 1. key in dict    返回bool
# 2. dict.get(key,[指定value])  不存在返回None，存在返回value，或者返回指定value
# print(type('lee' in dict1))

# print(dict1.get('zhang'))

# set 集合
set1 = {1, 2, 3}


def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


#
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# 判断一个对象是可迭代对象
from collections.abc import Iterable

print(isinstance('abc', Iterable))
# enumerate 将list转换为index，value对
for index, value in enumerate(['A', 'B', 'C', 'D']):
    print(f'index:{index},value:{value}')


def findMinAndMax(L):
    maxNum = None
    minNum = None
    if len(L) == 0:
        maxNum = None
        minNum = None
    else:
        maxNum = L[0]
        minNum = L[0]
        for value in L:
            if value > maxNum:
                maxNum = value
            if value < minNum:
                minNum = value
    return minNum, maxNum


# 列表生成式
list_1 = [x * x for x in range(1, 10)]
print(list_1)

list_2 = [m + str(n) for m in 'ABCD' for n in [1, 2, 3, 4]]
print(list_2)

import os

dir_list = [dir for dir in os.listdir('.')]
print(dir_list)


def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]


# 1 [1]
# 2 [1,1]
# 3 [1,2,1]
# 4 [1,3,3,1]


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
import json


def normalize(name):
    result = map(lambda text: text[:1].upper() + text[1:].lower(), name)
    return list(result)


normalize(['adam', 'LISA', 'barT'])

from functools import reduce


def prod(L):
    return reduce(lambda x, y: x * y, L)


print(prod([3, 5, 7, 9]))


def str2float(s):
    dot_index = s.index('.')
    s_len = len(s)
    return reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), s.replace('.', ''))) / (
            10 ** (s_len - 1 - dot_index))

# print(str2float('1234.123'))
