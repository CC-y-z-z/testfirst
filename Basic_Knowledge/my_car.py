from car import Car
my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23#1
# my_new_car.update_odometer(23)#2
my_new_car.read_odometer()