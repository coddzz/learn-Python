import math

# Datatypes
# Boolean data type (True or False)
x = True
y = bool(False)
print(y)
print(type(y))


# Numeric # integers
price = 100
best_price = int(90)
print(type(price))
print(isinstance(best_price, int))


# float type
mark = 61.28
mark2 = float(72.54)
print(type(x))


# complex Numbers
value = 5+3j
print(type(value))
print(value.real)
print(value.imag)


# math Functions
num = 21.62
print(abs(num))
print(abs(num * 2))
print(round(num))

print(math.pi) #pi value
print(math.sqrt(64)) # Square root
print(math.ceil(num)) 
print(math.floor(num))


# String to a number
number = "2000" 
print(type(number)) #string value
print(type(int(number))) #int value