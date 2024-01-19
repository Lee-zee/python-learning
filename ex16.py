# 重写文件
from sys import argv

script, filename = argv 

base_url = './public/text/'

print(f"是否清空该文件 {filename}")
print("取消请按 CTRL-C")
print("确认请按 RETURN")

input("?")

print("正在打开文件")
target = open(base_url+filename,'w')

print("清空文件，再见")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file")

target.write(line1) 
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("写入完成，关闭文件")

target.close()