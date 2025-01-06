alien_0={'color':'green','points':5}
# a=input()
# print(a)
print(alien_0['color'])
print(alien_0['points'])
#射杀外星人所获得的分数
new_points=alien_0['points']
print(f"You just earned {new_points} points!")
#添加键值对
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
#删除键值对
del alien_0['points']
print(alien_0)
#访问值，使用get，防止出现键值错误
point_value=alien_0.get('points','No point value assigned.')
print(point_value)