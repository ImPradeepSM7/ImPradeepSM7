'''
# Data types :
1. Integer - 10, 1, 20, 20
2. Float - 100.20, 128.546
3. boolean- True, False
4. string - 'name', "sal", "address", "10", "100.56" , "True"



'''
# Functions
# print(x) - To print the given data in console
# type()  - To find the type of variable
# id()    - To find variable referring address

x = 10  # create operation / write operation
#x = 10+20+30

print(x) # read operation

x = y = z =10   # possible

# x =100
# x =200 # not possible at  a time

print("x")
print("Type of x : ", type(x))
print("Id of x   : ", id(x))

x = 10 + 20 - 45 * 43 / 2  # BODMAS Rule
print("final value:", x)
print("Type of x : ", type(x))
print("Id of x   : ", id(x))

is_active = True # 1 represents True, 0 Represents False
print("Type of is_active : ", type(is_active))
print("ID of is_active   : ", id(is_active))

x = 10
print("integer:", type(x), id(x))
y = 10.0
print("float:", type(y),id(y))
str = '10'
print("Type of str:", type(str), id(str))

# Type conversions

print("----Type conversions--------")
'''
a = 121.23

int() print(int(a))
float()
complex()
bool()
'''
a = 0
print(bool(a))
print("converting int to float")
x = 10
print("value : ",x, type(x))
# Convert to float
y = float(x)
print("value : ",y, type(y))

print("converting int to boolean")
x = 0
print(x, type(x))
y = bool(x)
print(y, type(y))
print("-------------------")
x = 14
print(x, type(x))
x = bool(x)
print(x, type(x))
print("-------------------")
x = 0
print(x, type(x))
x = bool(x)
print(x, type(x))





eid = "10001"
print(eid, type(eid))

scan_code = 'abc32'



# collections, group of invidual elements

#list [], tuple (), set {}, dict{"key":"value", }, str '', "",




x = 300
y = 300

print(id(x), id(y))