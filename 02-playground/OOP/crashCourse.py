class Restaurant():

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('restaurant name : ' + self.restaurant_name)
        print('cuisine type : ' + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")

restaurant = Restaurant('Pizza hut' , "sushi")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 5
print(restaurant.number_served)
