# 文件读取

from sys import argv
script, filename = argv

base_url = './public/text/'

text = open(base_url + filename)

print(f"文件名:{filename}")
print(text.read())

print("再次输入文件名:")
filename_again = input("> ")

text_again = open(base_url+ filename_again)
print(text_again.read())