
'''
Datatypes
numbers  : int float
boolean  : True False
'''

# STRING  # Group of characters
'''
Registration Form
=====================
EID         : 2343       -- int 
First name  : 'Madhu'      -- String
Last name   : 'Nettem'     -- String
DOB         : 'XXXXX'      -- String
Contact no  : '4312432'    -- String
MailID      : 'fsadsfsdf@gmail.com' -- String
Password    : 
'''

str1 = 'Hello World'  # "Hello World"
#   012345678910
#                 -3-2-1
x = y = 10
# 2 = 3 = l
print(str1)
print(type(str1), id(str1))

print(id(str1), id(str1[0]), id(str1[2]))
print("l mem location:", id(str1[2]),id(str1[3]), id(str1[9]) )





ch = 'A'  # "A"
print(ch)

ch = "1"  # "1"
print(ch+"2") # join/concatnate
print(ch, type(ch))
print("Addition :", int(ch)+2)

ch = '1.5'
#5kgs oil + 2dozen
print("Addition : ", float(ch)+2.7) # 1.52.7

ch = '*'
print(ch, type(ch))


# Litres ML
# KM M  CM MM
# KG Grams MG
# Litres KM KG  --< Not Possible
print("-----Conversions----------")
x = 10
y = "20"
#print(x+y)
print(x, y, type(x), type(y))

if type(x) == type(y):
    print("Addition :", x+y)
else:
    print("Addition is not possible")


'''
Data Structures:  
----------------
Set 
Matrix 
Sequence and Series
'''
x = 10
print("------------String for loop------------")
for char in 'Hello World':  # A 65 a 97
    print(char)
print()
print("------------CRUD Operations------------")
# CRUD Operations
x = 10     # CREATE    Write operation
print(x)   # RETRIEVE  Read operation
x = 20     # UPDATE
del x      # DELETE





msg = 'Hello World'
msg1 = 'Hello World'
print(msg, msg1, id(msg), id(msg1))

msg = 'python'

