age=12

# if age<4:
#     print("Your admission cost is $0.")
# elif age<18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")

if age<4:
    price=0
elif age<18:#可多次使用
    price=25
else:#可省略
    price=40
print(f"Your admission cost is ${price}.")