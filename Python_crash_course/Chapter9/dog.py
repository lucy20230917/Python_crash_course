class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

my_dog.sit()
my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()


print(f"My dog's name is {my_dog.name}.")
print(f"My dog id {my_dog.age} years old.")


print(f"\nYour dog's name is {my_dog.name}.")
print(f"Your dog id {my_dog.age} years old.")