#__init__ -> Constructor
#__str__ -> Print the object as a string each time it is called instead of the address in memory
# self -> Refers to the object, the javascript this
# __ in front of variables or methods we make them private
# method = function object

class Animal():
    
    def __init__(self):
        self.__tipo = 'dog'
        self.__years = 5
        self.__is_male = True
        
    def __str__(self):
        if (self.__is_male):
            gender = 'male'
        else:
            gender = 'female'
        return "I am a {0} {1} and I am {2} years old".format(gender, self.__tipo, self.__years)

    def __private_function(self):
        print("I am a private method")
        
    def call_function(self):
        self.__private_function()
        
perro = Animal()

print(perro)
perro.call_function()