def get_formatted_name(first_name, last_name):
    '''返回整洁的姓名'''
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name,middle_name,last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
