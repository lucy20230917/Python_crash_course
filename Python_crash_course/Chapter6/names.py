#人
name_0 = {'first_name': 'jordan', 
         'last_name': 'bruno',
         'age': 28,
         'city': 'coventry'}

print("Here is the user's information: ")
print(name_0['first_name'])
print(name_0['last_name'])
print(name_0['age'])
print(name_0['city'])

name_1 = {'first_name': 'lucy', 
         'last_name': 'liu',
         'age': 22,
         'city': 'hainan'}

name_2 = {'first_name': 'james', 
         'last_name': 'boomington',
         'age': 28,
         'city': 'coventry'}

people = {'bjordan': name_0, 
         'llucy': name_1,
         'bjames': name_2, }

for username, user_info in people.items():
    print(f"\nUsername: {username} ")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    city = user_info['city']
    age = user_info['age']

    print(f"\tFull_name: {full_name.title()}")
    print(f"\tCity = {city.title()}")
    print(f"\tAge = {age}")


print(people)



#喜欢的数
favorite_numbers = {
           'jordan': 28,
           'lucy': 7, 
           'james': 18,
           'ade': 10,
           'paul': 24,}
for name, num in favorite_numbers.items():
    print(f"\nName: {name}")
    print(f"Num: {num}")

#词汇表
vocal = {'apple': '苹果',
         'banana': '香蕉',
         'organe': '橘子',
         'grape': '葡萄',}
print('\nHere is the vocal list:')
for eng,ch in vocal.items():
    print(f"{eng}: {ch}")

vocal['cat'] = '猫'
vocal['dog'] = '狗'
vocal['hat'] = '帽'
vocal['fish'] = '鱼'
vocal['bird'] = '鸟'

print('\nHere is the new vocal list:')
for eng,ch in vocal.items():
    print(f"{eng}: {ch}")

#river
rivers = {'nile': 'egypt', 
          'amazon': 'brazil', 
          'yangtze': 'china',
          }

print("Here is the information about rivers: ")
for rive,country in rivers.items():
    print(f"The {rive.title()} runs though {country.title()}")

for rive in rivers.keys():
    print(rive.title())

for country in rivers.values():
    print(country.title())


#pets
