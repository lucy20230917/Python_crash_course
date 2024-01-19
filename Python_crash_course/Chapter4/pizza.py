pizzas = ['pepperoni', 'sasuage', 'mushrooms']
for pizza in pizzas:
    print(pizza)
    print(f"I like {pizza} pizza.")
print("i really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append("onions")
friend_pizzas.append("bacon")
print(pizzas)
print(friend_pizzas)

print("My favorite pizzas are:")
for my_pizza in pizzas:
    print(my_pizza)

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
