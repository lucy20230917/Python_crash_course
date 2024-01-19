for value in range(1,21):
    print(value)

numbers = list(range(1,1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,21,2))
print(odd_numbers)

divisible_by_three = [num for num in range(3,31) if num % 3 == 0]
for dividible in divisible_by_three:
    print(dividible)

cubes = [ cube ** 3 for cube in range(1,11)]
print(cubes)

