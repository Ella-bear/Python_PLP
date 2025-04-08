class Car:
    color = "black"  # class attribute
    model = "BMW X5"  # class attribute
    year = 2024  # class attribute
    price = "$65,200"  # class attribute

    # constructor method to initialize objects of the class
    # self refers to the instance of the class
    def __init__(self, color, model, year, price):
        self.color = color  # instance attribute
        self.model = model  # instance attribute
        self.year = year  # instance attribute
        self.price = price  # instance attribute

# Create an instance of the Car class
carDetails = Car("black", "BMW X5", 2024, "$65,200")

print(carDetails.color)  
print(carDetails.model)  
print(carDetails.year)   
print(carDetails.price)  

# Polymorphism 
class Snake:
    def sound(self):
        return "Hiss!"

for animal in [Snake()]:
    print(animal.sound())