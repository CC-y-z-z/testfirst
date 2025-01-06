unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()#从末尾删除一个，并将其赋值给变量
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)#将删除的用户添加到已验证列表中
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
