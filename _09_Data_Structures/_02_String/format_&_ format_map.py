




# Python3 program to demonstrate
# the str.format() method

'''
Syntax : { } .format(value)

Parameters : 
(value) : Can be an integer, floating point numeric constant, string, characters or even variables.
Returntype : Returns a formatted string with the value passed as parameter in the placeholder position. 
'''
# using format option in a simple string
print("{}, A computer science portal for geeks."
	.format("GeeksforGeeks"))

# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))

# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))


# multiple
'''
Syntax : { } { } .format(value1, value2)

Parameters :  (value1, value2) : Can be integers, floating point numeric constants, strings, 
characters and even variables. Only difference is, the number of values passed as parameters 
in format() method must be equal to the number of placeholders created in the string.

Errors and Exceptions : 

IndexError : Occurs when string has an extra placeholder, and we didn’t pass any value for it in the format() method. 
Python usually assigns the placeholders with default index in order 
like 0, 1, 2, 3…. to access the values passed as parameters. 
So when it encounters a placeholder whose index doesn’t have any 
value passed inside as parameter, it throws IndexError. 



'''

# Python program demonstrating Index error

# Number of placeholders are four but
# there are only three values passed

# parameters in format function.
my_string = "{}, is a {} {} science portal for {}"

print(my_string.format("GeeksforGeeks", "computer", "geeks", 12))


# Python program using multiple place
# holders to demonstrate str.format() method

# Multiple placeholders in format() function
my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))

# different datatypes can be used in formatting
print("Hi ! My name is {} and I am {} years old"
	.format("User", 19))

# The values passed as parameters
# are replaced in order of their entry
print("This is {} {} {} {}"
	.format("one", "two", "three", "four"))




'''
Python String format_map() Method

Python String format_map() method is an inbuilt function in Python, which is used to return a dictionary key’s value.

'''


# Example 1: Python String format_map() method

# input stored in variable a.
a = {'x':'John', 'y':'Wick'}
  
# Use of format_map() function
print("{x}'s last name is {y}".format_map(a))



# Example 2:

# input stored in variable a.
a = {'x':"geeksforgeeks", 'y':'b'}
  
# Use of format_map() function
print('{x} {y}'.format_map(a))


# Input dictionary
profession = { 'name':['Barry', 'Bruce'],
               'profession':['Engineer', 'Doctor'],
               'age':[30, 31] }
                       
# Use of format_map() function 
print('{name[0]} is an {profession[0]} and he'
      ' is {age[0]} years old.'.format_map(profession))
        
print('{name[1]} is an {profession[1]} and he'
      ' is {age[1]} years old.'.format_map(profession))

# Example 4: Practical Application
# The format_map() function can be used in any practical application.


# Python code showing practical
# use of format_map() function
def chk_msg(n):

    # input stored in variable a.
    a = {'name':"George", 'mesg':n}

    # use of format_map() function
    print('{name} has {mesg} new messages'.format_map(a))

chk_msg(10)

