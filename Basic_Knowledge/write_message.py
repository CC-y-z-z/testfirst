filename='prpgramming.txt'
with open(filename,'w') as file_object:#w写入；r读取；a附加；r+读写；无模式实参 只读
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large detasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")