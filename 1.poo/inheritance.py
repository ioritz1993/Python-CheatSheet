class Animal():
    
    def __init__(self, name, years, is_male):
        self.__name = name
        self.__years = years
        self.__is_male = is_male
        
    def __str__(self):
        if (self.__is_male):
            gender = 'male'
        else:
            gender = 'female'
        return "I am a {0} {1} and I am {2} years old".format(gender, self.__name, self.__years)

class Dog(Animal):     
    pass
    
dog = Dog('sausage dog', 2, False)
print(dog)