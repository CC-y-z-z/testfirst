filename='alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
#在系统的默认编码与要读取的文件使用的编码不一样时，须给encoding指定值
        contents=f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")