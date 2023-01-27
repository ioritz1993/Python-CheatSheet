import re

text = "Below is a string of text. For this we will carry out a search for the letter a."

text_find = "a"

print("{} matches found ".format(len(re.findall(text_find, text))))