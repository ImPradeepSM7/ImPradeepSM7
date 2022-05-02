
'''
Syntax :
------------
# for loop syntax
        for <var> in <sequence>:
           # statements

string list tuple



'''
'''
numbers system -1,-2/4, 34.4, 56, 3 4/5, 0 ,00
advanced concepts : Sequence,Series  1 to 100 -- n(n+1)/2
                  : Sets {1,2,3} U {2,3,4}
                  : Matrix []


'''

# 1. Find sum of numbers from 1 to 100
    # Using while
i = 1
while i < 101:
    pass





# Data Types
x = 10  # integer
x = 10.5 # float  complex long
is_male = True # boolean

# Data structures
message = "Hello World"  # String
numbers = [1, 2, 3, 4, 5]  # list
numbers = (1 ,2 ,3 ,4 ,5)  # tuple
emp_details = {'eid': 100, 'name' :'Madhu' ,'sal' :1000}  # Dictionary
emp_ids = {1 ,2 ,3 ,4 ,5 ,6}   # Set

print("---------String--------------")
# for loop with strings
message = "Hello World"
print(message)
for char in message:  # 2 hours  Iterator Generator  Decorator
    print(char)
print("End of for loop")

number = "12345"
for num in number: # "1" "2" "3"
    print(num)

print("---------List--------------")
# for loop with list
numbers = [1, 2, 3, 4, 5]
for value in numbers: # 1 2 3 4 5
    print(value)
print("End for loop")

numbers = ['1', '2', '3', '4', '5']
for value in numbers: # '1' '2' '3' '4' '5'
    print(value)
print("End for loop")

numbers = (1 ,2 ,3 ,4 ,5)

print("---------Tuple--------------")
for val in numbers:
    print(val)

print("---------Dictionary--------------")
emp_details = {'eid' :100 ,'name' :'Madhu' ,'sal' :1000}

print("----Items-----")
for key ,val in emp_details.items():
    print(key ," : ", val)

print("----Keys------")
for key in emp_details.keys():
    print(key)

print("-----Values-----")
for val in emp_details.values():
    print(val)

print("---------Set--------------")
emp_ids = {1, 2, 3, 4, 5, 6}
for eid in emp_ids:
    print(eid)
