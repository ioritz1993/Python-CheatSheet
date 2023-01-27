
# It is used as yield but for navigating two-dimensional arrays

def get_letter_for_element(*datos):
    for elemento in datos:
        for subElemento in elemento:
            yield subElemento

        
def get_letter_for_element_with_yield_from(*datos):
    for elemento in datos:
        yield from elemento

        
letters_returned = get_letter_for_element_with_yield_from("abc", "def", "ghi")

print(next(letters_returned))
print(next(letters_returned))
print(next(letters_returned))
print(next(letters_returned))
print(next(letters_returned))