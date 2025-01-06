# pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# #删除为特定值的所有列表元素

# def describe_pet(animal_type,pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hanster','harry')
# describe_pet('dog','willie')
# describe_pet(animal_type='cat',pet_name='anay')
# describe_pet(pet_name='anay',animal_type='cat')

def describe_pet(pet_name,animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
describe_pet(animal_type='cat',pet_name='anay')
describe_pet(pet_name='anay',animal_type='cat')