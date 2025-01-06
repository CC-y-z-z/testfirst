squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)#将新计算得到的平方值附加到列表squares末尾
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
squares=[value**2for value in range(1,11)]#列表解析
print(squares)