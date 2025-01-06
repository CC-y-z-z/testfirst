#在字典中储存列表
# pizza={
#     'crust':'thick',
#     'toppings':['mushrooms','extra cheese']
# }
# print(f"You ordered a {pizza['crust']}-curst pizza "
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t"+topping)

def make_pizza(size,*toppings):#*toppings空元组
    print(f"\nMakeing a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')