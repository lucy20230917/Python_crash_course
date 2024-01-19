#pizza
prompt = "\nEnter the pizza topping you want to add:"
prompt += "\n(Enter 'quit' when you are finished)"

while True: 
    pizza_topping = input(prompt)

    if pizza_topping == 'quit':
        print("Have a nice day!")
        break

    else: 
        print("is there anything you want to add in the top of pizza?")

#cinema tickets

prompt_0 = "\nEnter your age: "
prompt_0 += "\n(Enter 'quit' if you don't want to buy a ticket.)"

while True:
     user_input = input(prompt_0)

     if user_input.lower() == "quit":
         break

     try:
         age = int(user_input)
    
         if age <3:
             print('You can have a free ticket!')
         elif age <= 12:
             print('You need to pay $10 to get a ticket.')
         else:
             print('You need to pay $15 to get a ticket.') 
             
     except ValueError:
         print("Please enter a valid age or 'quit'.")
