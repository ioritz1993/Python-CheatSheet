import re

example_list = [
    'www.example1.com',
    'www.example2.es',
    'example3.com',
    'example4.es',
    'Example5.es',
    'exaAmplE5.es'
    ]

print("Data containing letters between s and t")
for element in example_list:
    if re.findall('[s-t]', element):
        print(element)
      
print()
print("Data containing letters between A and F")
for element in example_list:
    if re.findall('[A-F]', element):
        print(element)
