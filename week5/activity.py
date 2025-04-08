#polymorphism
class Bike:
    def ride(self):
        return "Riding a bike!"
    
class Lion:
    def ride(self):
        return "Roar!"
    
for obj in [Bike(), Lion()]:
    print(obj.ride())

