# Abstract class cannot be instantiated directly. Define the structure of other classes

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def movement(self):
        pass
    
    @abstractmethod
    def number_wheel(self):
        print('I have wheels')

        
class Motorbike(Vehicle):

    def movement(self):
        print('The motorbike moves')
        
    def number_wheel(self):
        super().number_wheel()
        print('I have two wheels')
        
motorbike = Motorbike()
motorbike.movement()
motorbike.number_wheel()
