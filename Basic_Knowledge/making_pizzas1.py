# #导入整个模块
# import pizza
# #使用函数module_name.function_name()
# pizza.make_pizza(16,'pepperoni')
# pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#使用as给模块指定别名
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')