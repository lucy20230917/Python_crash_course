favorite_languages = {
                      'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():   #for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends: 
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("\nErin, please take out poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):  #set()找出所有种类
    print(language.title())

new_favoriate_languages = {
                      'james': 'python',
                      'lucy': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }
for new_favoriate_language in new_favoriate_languages.keys():
    if new_favoriate_language in favorite_languages.keys():
        print(f"{new_favoriate_language.title()},thank you for join in this investigation.")
    else:
        print(f"{new_favoriate_language.title()},please join in this investigation.")


favorite_languages = {
                      'jen': ['python','ruby'], 
                      'sarah': ['c'], 
                      'edward': ['ruby', 'go'], 
                      'phil': ['python', 'haskell'], 
                      }

for name, languages in favorite_languages.items():
    print(f"\n {name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")



    

