names = ['ada', 'lucy', 'alen','adam']
print(f'{names[0].title()}, sorry to hear that you are not comming.')

names[0] = 'aggie'
print(names)
print(f'{names[0].title()}, you are invited.')


names.insert(0, 'albin')
print(names)

names.insert(2, 'jordan')
print(names)

names.append('james')
print(names)

while len(names)>2:    #循环
    popped_name1 = names.pop()
    print(names)
    print(f'{popped_name1.title()}, sorry to inform you, you are uninvited.')
    

print(names)
print(f'{names[0].title()}, you are invited.')
print(f'{names[1].title()}, you are invited.')


del names[0]
print(names)
del names[0]
print(names)