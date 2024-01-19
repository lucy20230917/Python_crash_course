locations ={}

investigation_active = True
while investigation_active:
    name = input("\nWhat is your name?")
    location = input("\nIf you could visit one place in the world. where would you go? ")

    locations[name] = location

    repeat = input("would you like to let another person respond?(yes/no)")
    if repeat == 'no':
         investigation_active = False

print("\n--- Poll Result ---")
for name,location in locations.items():
    print(f"{name.title()} would like to visit {location.title()}")


