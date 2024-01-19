#sandwich
def sandwich(*ingredients):
    print(f"\nMaking a sandwich with the following ingredient: ")
    for ingredient in ingredients:
        print(f"- {ingredient}")

sandwich('egg','cheese')

#user_info
def build_profile(first, last, **user_info):
    '''创建一个字典，其中包括我们知道的有关用户的一切。'''
    user_info['first_name'] = first
    user_info['Last_name'] = last
    return user_info



user_profile = build_profile('lucy', 'liu',
                             location = 'coventry',
                             field = 'e-bussiness management',
                             live = 'the oaks'
                             )

print(user_profile)

#cars
def make_car(manufacturer, model, **car_info):
    car_info["Manufacturer"] = manufacturer
    car_info['Model'] = model
    return car_info

car = make_car('subaru', 'outback', color ='blue', tow_package=True)

print(car)
