motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #修改列表元素
print(motorcycles)

motorcycles.append('honda') #列表末尾添加元素
print(motorcycles)

motorcycles.insert(0, 'harley') #在列表中插入元素
print(motorcycles)

del motorcycles[0] #删除列表中第一个元素
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle) #删除列表中最后的元素

first_owned = motorcycles.pop(0) #删除列表中指定元素
print(f"The first motorcycle i owned was a {first_owned.title()}.")

motorcycles.append('honda') #列表末尾添加元素
print(motorcycles)

motorcycles.remove('suzuki') 
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")
print(f"\nA {too_expensive.title()} is too expensive for me.")