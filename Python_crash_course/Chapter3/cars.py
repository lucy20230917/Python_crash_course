cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) #按字母临时排序

cars.sort()  #按字母永久排序
print(cars)

cars.sort(reverse = True) #按字母相反永久排序
print(cars)

cars.reverse()
print(cars)

len(cars)