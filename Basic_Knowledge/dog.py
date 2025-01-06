class Dog:
    def __init__(self,name,age):#类中的函数称为方法，两边都有两个下划线，会被自动调用
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")
my_dog=Dog('Willie',6)
your_dog=Dog('Lucy',3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()