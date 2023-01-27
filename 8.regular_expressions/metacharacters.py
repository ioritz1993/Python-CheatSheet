import re

example_list = [
    'www.example1.com',
    'www.example2.es',
    'example3.com',
    'example4.es',
    'example5.es'
    ]

print("Find data starting with www")
print("=========================================")
for element in example_list:
    if re.findall('^www', element):
        print(element)
        
print()
print("Find data end with es")
print("=========================================")
for element in example_list:
    if re.findall('es$', element):
        print(element)
        
print()
print("Find if it contains the letter s")
print("=========================================")
for element in example_list:
    if re.findall('[s]', element):
        print(element)
        
print()
print("Find if it contains the letter example4.es or example5.es")
print("=========================================")
for element in example_list:
    if re.findall('example[45].es', element):
        print(element)