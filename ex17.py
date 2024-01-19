# 复制文件
from sys import argv 
from os.path import exists

script,from_file,to_file = argv

base_url = './public/text/'

from_file = base_url + from_file
to_file = base_url + to_file

print(f"从{from_file}复制到{to_file}")

indata = open(from_file,encoding="utf-8").read()

print(f"The input file is {len(indata)} bytes long")

# print(f"输出文件存在吗？{exists(to_file)}")

open(to_file,'w',encoding="utf-8").write(indata)

print("写入完成")
