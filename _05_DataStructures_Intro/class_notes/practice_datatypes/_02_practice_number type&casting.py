# number_type
x = 15
y = 10.5
z = 1j
print(type(x))  # int
print(type(y))  # float
print(type(z))  # complex
print(id(x))
print(id(y))  # memory location
print(id(z))
print(x)
print(y)
print(z)

# int
x = 12
y = 115441444
z = -96
print(type(x))
print(type(y))
print(type(z))

# float
x = 10.25
y = 12515455.336645
z = 77.232
print(type(x))
print(type(y))
print(type(z))

x = 12e4
r = 36E45
m = -396E456
print(type(x))
print(type(r))
print(type(m))

# Complex type

e = 3 + 8j
t = 6j
y = -8j
print(type(e))
print(type(y))
print(type(t))

# Type_conversion
# complex_numbers are not converted into another type
x = 10  # int
y = 15.5  # float
z = 5j  # complex

a = float(x)
b = complex(y)
c = int(y)

print(type(a))
print(type(b))
print(type(c))
print(a)
print(b)
print(c)

import random

print(random.randrange(1, 10))
print(random.randrange(560, 1200))
print(random.randrange(10, 200))
print(random.randrange(1000, 8900))

# specify the type of variable

x = int(56)
y = int(58.32)
r = int("3")
print(type(x))
print(type(y))
print(type(z))
print(x)
print(y)
print(z)

m = float(10)
f = float(56.32)
c = float("89")
print(m)
print(r)
print(c)
print(type(c))
print(type(r))
print(type(m))

d = str(10)
x = str(56.256)
b = str("3")
t = str("mani")
print(d)
print(x)
print(b)
print(t)
print(type(d))
print(type(x))
print(type(b))
print(type(t))

# data types

# text type_strings:"hello"
# numeric_type:int=10,
# float=10.25,
# complex=1+2j

# sequence_type:
# tuple=("apple", "banana"),ordered,allow duplicate keys,immutables
# lists=["apple", "banana"],ordered,allow duplicate keys,mutable,changeable
# Range(6)

# mapping_type
# dictionaries={name="hari",age=36},ordered,not allowed,changeable

# sets type
# sets ={"apple", "banana"},unordered,not allowed,not changeable
# frozenset=frozenset{"apple", "banana"}

# boolean type=bool

# Binary type
# bytes(6)
# bytearray(6)
# memory view(bytes(10))
