print('Pastrami sandwich has been sold out.')
sandwich_orders = ['classic','pastrami','veggie','pastrami','spicy','pastrami']
finished_sandwiches = []

while sandwich_orders:
         finished_sandwich = sandwich_orders.pop()

         if finished_sandwich != 'pastrami':
            print(f"I made your {finished_sandwich.title()} sandwich")
            finished_sandwiches.append(finished_sandwich)
         else:
               print("Sorry, we don't have pastrami sanwish now.")

print(finished_sandwiches)

print("Your orders are finished.")
