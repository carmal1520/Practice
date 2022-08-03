# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_resturant(self):
#         rest_name = f"{self.name}"
#         food_type = f"{self.cuisine_type}"
#         statement = f"Welcome to {rest_name.title()}, we sell {food_type} food."
#         return statement

#     def open_restaurant(self):
#         msg = f"{self.name} is open"
#         return msg
    
#     def set_number_served(self, update_number_served):
#         self.number_served = update_number_served

#     def increment_number_served(self, served):
#         self.number_served += served

# class IceCreamStand(Restaurant):
#     def __init__(self, name, cuisine_type):
#         super().__init__(name, cuisine_type)
#         self.flavors = ["Strawberry", "Chocolate", "Vanilla"]

#     def icecream_flavors(self):
#         print(f"{self.flavors}")

