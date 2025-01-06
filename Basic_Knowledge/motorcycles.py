motorcycles=['honda','yamaha','suzuke']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
motorcycles.append('honda')#在末尾增加元素
print(motorcycles)
motorcycles.insert(0,'a')#可以插入任意位置
print(motorcycles)
del motorcycles[0]#知道要删除的元素在列表中的位置，可以删除任意一个元素
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycle=motorcycles.pop()#()中无信息时，弹出最后一个，该元素还可调用
print(motorcycles)
print(popped_motorcycle)
first_owned=motorcycles.pop(0)#可以弹出任意一个元素，该元素还可调用
print(f"The first motorcycle I owned was a {first_owned.title()}.")
motorcycles=['honda','yamaha','suzuke']
motorcycles.remove('honda')#知道要删除元素的值，可以删除任意一个元素
print(motorcycles)
too_expensive='yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
motorcycles=['honda','yamaha','suzuke']
print(motorcycles[-1])#索引-1总是返回最后一个列表元素