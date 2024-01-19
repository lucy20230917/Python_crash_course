class Restaurant:
    def __init__(self,restaurant_name,restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type
        self.number_served = 0
        
    def  describe_restaurant(self):
        print(f"The restaurant name's {self.name}.")
        print(f"It's {self.type} food.")

    def open_restaurant(self):
        print(f"{self.name} is opening.")

    def set_number_served(self, customers_number):
        self.number_served = customers_number
        print(f"The restaurant currently has a reservation for {self.number_served} people")

        
    def increment_number_served(self, number_of_diners):
        self.number_served += number_of_diners
        print(f"The restaurant may receive {self.number_served} people a day")
        


restaurant = Restaurant('Art center', 'india')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(10)
restaurant.increment_number_served(10)





