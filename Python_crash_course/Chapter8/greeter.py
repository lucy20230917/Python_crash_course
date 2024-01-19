def greet_user():
    '''显示简单的问候语'''
    print("Hello!")

greet_user()

def greet_user(username):
    '''显示简单的问候语'''
    print(f'Hello,{username.title()}!')

greet_user('jesse')

def display_message():
    print('I am happy!')

display_message()

def favorite_book(title):
    print(f"My favorite book is <<{title}>>")

favorite_book("the old man and the sea")

def get_formatted_name(first_name, last_name):
    '''返回整洁的名字'''
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True: 
    print(("\nPlease tell me your name:"))
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\Hello, {formatted_name}!")
