import math

word = "Hello World"

word += "!"
print(word);


# Paragraph lines
para = '''

HELLO WORLD !!!
\t Python is widely-used, general-purpose, high-level programming
language, known for its readability and versatility,
Developed by Guido van Rossum and first released in 1991. \n
https://github.com/coddzz

'''
print(para)
print(para.lower()) #Lowercase
print(para.upper()) #Uppercase

print(para.replace("HELLO WORLD","PYTHON"))
print(para) 


print("length of the word \'Hello\': ",len("Hello"))

# list some Marks
title = "Marks".upper()
print(title.center(20, "="))
print("English".ljust(16, ".") + "80".rjust(4))
print("Maths".ljust(16, ".") + "75".rjust(4))
print("Science".ljust(16, ".") + "75".rjust(4))

# Index values
print(word[1])
print(word[-1])
print(word[1:-1])
print(word[1:])

# Methods return booleanword data
print(word.startswith("H"))
print(word.endswith("D"))

