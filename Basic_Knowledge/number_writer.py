import json
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)#用json.dump储存数字列表