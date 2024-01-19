# 输出输入两数之和
# num1 = float(input("请输入数值1\n"))
# num2 = float(input("请输入数值2\n"))
# print("两数之和是:",int(num1+num2))

# 输出1-100
# for n in range(1,101):
#     print(n)

# 1加到100的和
# total = 0
# for n in range(1,101):
#     total += n
# print(total)

# 输入一个值，输出以这个值为公比，1为首项的等比数列前10项
# ratio =  int(input("请输入公比：\n"))
# num = 0
# preNum = 1
# while num <= 10:
#     print(preNum)
#     preNum *= ratio
#     num+=1

# 输入一个大于等于3的值n，输出斐波纳契数列的前n项。注：斐波纳契数列：1,1,2,3,5,8,13,21...
# n =  int(input("请输入n,n不小于3：\n"))
# pre = 1
# cur = 1
# index = 0
# while index < n:
#     index += 1
#     if index == 1 or index == 2:
#         print(1)
#     else:
#         next_cur = pre + cur
#         pre = cur
#         cur = next_cur
#         print(cur)

# 输入一个大于等于1的值n，输出星号（*）组成的等腰三角形，底边长为n
# n =  int(input("请输入n,n不小于1：\n"))
# for i in range(1, n+1):
#     print(" "*(n-i)+"* "*i)

# 输出9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i) + "*" + str(j) +"=" + str(i*j),end="\t")
#     print("\n")

# 输入三个数，输出这三个数的最大值。
# num1 = float(input("请输入第一个数："))
# num2 = float(input("请输入第二个数："))
# num3 = float(input("请输入第三个数："))
# print('最大值是：',max(num1,num2,num3))

# 输出从1000以内，用3、5、7去除，余数均为2的正整数。
# for n in range(1,1001):
#     if n%3 ==2 and n%5 == 2 and n%7 == 2:
#         print(n)

# 求所有不超过200的N值，N的平方是具有对称性质的回文数
# for n in range(1,201):
#     square_n = n * n
#     if(str(square_n) == str(square_n)[::-1]):
#         print(n)

# from.txt是一个混杂了英文单词和中文的文本文件。
# 把from.txt里的文件复制到to.txt里，要求只复制其中的英文单词，并按字母序排序
import re
file = open('./public/text/from.txt', 'r',encoding='utf-8')
data = file.read()
file.close()
english_words = re.findall('[A-z]+', data)
print(english_words)
english_words.sort()
with open('./public/text/to.txt', 'w',encoding='utf-8') as f:
    for word in english_words:
        f.write(word+'\n')