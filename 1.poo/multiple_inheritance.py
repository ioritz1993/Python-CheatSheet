# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
class FictitiousCompany(object):
    company_name = "Ficticius Company"
    
class ChildClass(Person,FictitiousCompany):      
    def saludo(self):
        print("Hello, this is {0} and I am {1} years old.".format(self.name, self.age))
        print("I work {0}".format(self.company_name))
        print("I am a class that inherits from Person and FictitiousCompany. Bye!")
    
ioritz = ChildClass("Ioritz", 30)
ioritz.saludo()
