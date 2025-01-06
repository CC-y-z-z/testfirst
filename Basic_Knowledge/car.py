# cars=['audi','bmw','subaru','toyota']
# for car in cars:
#     if car=='bmw':
#         print(car.upper())#全大写
#     else:
#         print(car.title())#首字母大写

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self,mileage):#2/3
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):#3
        self.odometer_reading+=miles
# my_new_car=Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
# # my_new_car.odometer_reading=23#1
# # my_new_car.update_odometer(23)#2
# my_new_car.read_odometer()
        
# my_used_car=Car('subars','outback',2015)#3
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

class Battery:
    def __init__(self,battery_size=75):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    def get_range(self):
        if self.battery_size==75:
            range=260
        elif self.battery_size==100:
            range=315
        print(f"This cat can go about {range} miles on a full charge.")

class ElectricCar(Car):#圆括号内指定父类名称
    def __init__(self,make,model,year):
        super().__init__(make,model,year)#特殊函数，调用父类方法
        self.battery=Battery()
