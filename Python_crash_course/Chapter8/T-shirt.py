#t-shirt:
def make_shirt(size='L',words="I love Python"):
    print(f"This shirt's size is {size.title()}.")
    print(f"the words on it are : {words}.")

make_shirt("m","hello,world!")
make_shirt()

#cities
def describe_city(name,country):
    print(f"{name.title()} is in {country.title()}.")

describe_city('reykjavik','iceland')
