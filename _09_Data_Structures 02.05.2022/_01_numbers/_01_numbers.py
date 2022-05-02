
''''''
'''
# DATA TYPES
numbers  - individual values
boolean  - individual value
string   - group of values  'A'  '1'  '100'  '193.4'  'mani'

# DATA STRUCTURES
List **
Tuple 
Dictionary **
Set
string

Collections module : NamedTuple OrderedDict DefaultDict FrozenSet 
'''
# numbers
'''
int 
float
complex : 3i+4j
'''
# boolean
True
False


x = 10
print(x)   # f(x)
print("Value is :", x)

x = 10 + 20
# LHS = RHS


# Naming conventions
# variables always small letter

# REQ: Receive employee id and print it.

'''
Step 1: Receive employee id 
Step 2: Print it
'''
     # Hard coding the value :: Static way
e_id = 4325  # emp_id empid eid e_id   st_rno strno prod_id
print("Employee id : ", e_id)

     # Receive the value dynamically
e_id = input("Enter your employee id :")
print("Employee id : ", e_id)

'''
f(x) = 2x + 1  # Mathematics

Python function
def f(x):
    val = 2x + 1
    print(val)
'''

print("--------------------type--------------")
print("Type of 10 :", type(10))
eid = 100
print("Employee details : ", eid, type(eid))

eid = input("Enter employee id :")
print("Employee details : ", eid, type(eid))

eid = int(input("Enter employee id :"))
print("Employee details : ", eid, type(eid))

e_sal = float(input("Enter employee salary :"))
print("Employee details : ", e_sal, type(e_sal))

eid = 100
print("Employee id and it address : ", eid, id(eid))
msg = 'Hello World'
print("Message is : ", msg, type(msg), id(msg))



