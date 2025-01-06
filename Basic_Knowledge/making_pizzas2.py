#导入特定的函数from module_name import function_name0,function_name1,function_name2
# from pizza import make_pizza
# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')

#关键字as将函数重命名为指定的别名
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

#导入模块中的所有函数from module_name import *    (不建议使用)