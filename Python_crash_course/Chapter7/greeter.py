name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who are you, we can personalize the messags you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f'\nHello, {name}!')

age = input("How old are you?")
age = int(age)  #获取数值输入
print(age >= 18)

