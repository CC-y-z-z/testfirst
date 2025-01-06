# current_number=1
# while current_number<=5:
#     print(current_number)
#     current_number+=1

current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue#返回循环开头，并根据条件测试结果决定是否继续执行循环
    print(current_number)
