def describe_pet(animal_type,pet_name):
    '''显示宠物的信息'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')
describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet_0(pet_name, animal_type='dog'):
    '''显示宠物的信息'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_0(pet_name='willie')
describe_pet_0("willie")

describe_pet_0('harry','hamster')


