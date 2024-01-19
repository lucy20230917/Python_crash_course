users = ['lucy', 'admin','ade','jordan','james']

for use in users:
    if use == "admin":
        print(f"Hello {use}, would you like to see a status report?")
    else:
        print(f"Hello {use}, thank you for logging in again.")



if users == []:
    print("We need to find some users!")

while len(users) > 0:
    users.pop()
    print('We lose a customer.')

if users == []:
    print("We need to find some users!")



current_users = ['lucy', 'admin','ade','jordan','james']
current_users1 = [current_user.upper() for current_user in current_users]
current_users2 = [current_user.lower() for current_user in current_users]
current_users3 = [current_user.title() for current_user in current_users]
new_users = ['charles','martina','michael','Lucy','JORDAN']

for new_user in new_users:
    if new_user in current_users and current_users1 and current_users2:
        print(f"Sorry, {new_user} is used, please change another one.")
    else:
        print(f"{new_user.title()}, thank you for join in us.")
