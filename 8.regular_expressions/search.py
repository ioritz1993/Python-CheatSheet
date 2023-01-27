import re

text = "Below is a string of text. For this we will carry out a search for the letter a."
text_find = "out"

found_text = re.search(text_find,text)

print(found_text.start())
print(found_text.end())
print(found_text.span())
