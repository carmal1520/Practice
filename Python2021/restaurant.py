class Restaurant:

    def __init__(self, r_name, cuisine_type):
        self.r_name = r_name
        self.cuisine_type = cuisine_type
        self.number_served= 0

    def describe_restaurant(self):
        name = f"\nName: {self.r_name.title()}"
        cuisine = f"Cuisine Type: {self.cuisine_type}"
        print(name)
        print(cuisine)

    def open_restaurant(self):
        message = f"\n{self.r_name.title()} is open. Servering {self.cuisine_type}."
        print(message)

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, additional_served):
        self.number_served += additional_served


class IceCreamStand(Restaurant):

    def __init__(self, r_name, cuisine_type):
        super().__init__(r_name, cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        for x in self.flavors:
            print(x)

icecream = IceCreamStand("Mr. Softy", "Ice Cream")

icecream.flavors = ["Stawberry", "Vanilla", "Chocolate"]