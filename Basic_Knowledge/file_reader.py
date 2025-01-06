# with open('pi_digits.txt') as file_object:
#     contents=file_object.read()
# print(contents.rstrip())#rstrip删除字符串末尾的空白
# # 所打开的文件夹为目录！！！！！这很重要

# #逐行读取
# filename='pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line)#调用print会加上一个换行符

#创建一个包含文件各行内容的列表
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())