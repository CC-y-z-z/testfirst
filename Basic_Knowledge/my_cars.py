from car import Car,ElectricCar#从一个模块中导入多个类
my_beetle=Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())
my_tesla=ElectricCar('tesla','roadster',2019)
print(my_tesla.get_descriptive_name())

# import car #导入整个模块，再使用句点表示法访问需要的类
# my_beetle=car.Car('volkswagen','beetle',2019)
# print(my_beetle.get_descriptive_name())
# my_tesla=car.ElectricCar('tesla','roadster',2019)
# print(my_tesla.get_descriptive_name())

# from module_name import *   #导入模块中的所有类，不推荐使用