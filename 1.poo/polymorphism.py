class Vehicle():
    def displacement(self):
        print("I have four wheels")

        
class Motorcycle():
    def displacement(self):
        print("I have two wheels")

        
class Truck():
    def displacement(self):
        print("I have six wheels")

    
# With polymorphism, the vehicle received will be of a dynamic type, and in turn,
# will call the function that it has defined
def displacement_vehicle(vehicle):
    vehicle.displacement()    

miVehicle = Motorcycle()
miVehicle2 = Vehicle()
miVehicle3 = Truck()

displacement_vehicle(miVehicle)
displacement_vehicle(miVehicle2)
displacement_vehicle(miVehicle3)