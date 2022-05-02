x = (10+25-30)


'''
write operation:
-----------------------------------------

step -1 : Load the statement

step-2: Execution starts from R.H.S = L.H.S

step-3 : In R.H.S ,finds the type of data like int, float, boolean, str

step-4 : If any expression , it performs the operation.final value, 
it converts final value into binary format

step-5 : Binary value will be alloacted some memory

step-6 : Memory address will be reffered to varible


'''

print(x)
print(type(x))
print(id(x))

y = True
print(type(y))
print(id(y))


z = "str"
print(id(z), type(z))

a = 120.56
print(type(a), id(a))


print(x)  # read operation retrieving



x = 10  #when value has reference count
y = 10
z = 10

x = 100


'''
Rules/ validations:
1. _ or letters (lowercase)  # _name, name, _NAME
2. Dont use numbers           # 100 = 10
3. Dont use keywords ,special symbols
'''

x = 10
_name = 10
eid = 11
#EID = 10

x =100
print(x)


x = y = 10     # one value to multiple variables

# x=10=100

print(id(x),id(y) )

x = 20

print(id(x))


x = 10

print(id(x),type(x), x) # if ref count = o moves to garbage collection

x = 10
'''
# rules or validations to create variable:

1. we can use uppercase or lowercase  or _ eg. myname, MYNAME, _myname , Myname
2. cannot start with digit eg . 98 = 10, _12 = 10
3. Dont use keywords as variable name

'''


x =0.4
y = 0.2
print(id(x))
print(id(y))

sum = x+y
print(sum, id(sum))



