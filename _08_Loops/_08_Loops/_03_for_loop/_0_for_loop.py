'''
Python for loop
The for loop in Python is used to iterate the statements or a part of the program several times.


The syntax of for loop in python is given below.

for iterating_var in sequence:
    statement(s)

'''

print("----------Iterating string using for loop------------------")

str = "Python"
for i in str:
    print(i)

print("--------------Program to print the table of the given number----------")

list = [1,2,3,4,5,6,7,8,9,10]
list2 = [5, 10, 15, 12]

for i in list:
    for j in list2:
        val = i * j
        print(val,end = ',')

print(" Program to print the sum of the given list.")

list = [10,30,23,43,65,12]
x = 0
for i in list:
    x = x+i #(x += i)
print("The sum is:",x)

'''
The range() function
--------------------------

The range() function is used to generate the sequence of the numbers. 
If we pass the range(10), it will generate the numbers from 0 to 9. 
The syntax of the range() function is given below.

Syntax:

range(start,stop,step size)
The start represents the beginning of the iteration.
The stop represents that the loop will iterate till stop-1. The range(1,5) will generate numbers 1 to 4 iterations. It is optional.
The step size is used to skip the specific numbers from the iteration. It is optional to use. By default, the step size is 1. It is optional.

'''
# Consider the following examples:


print("Program to print numbers in sequence")

for i in range(10):
    print(i,end = ' ')

print(" Program to print table of given number")

n = int(input("Enter the number "))
for i in range(1, 11):
    c = n*i
    print(n,"*",i,"=",c)

print("Program to print even number using step size in range()")


n = int(input("Enter the number "))
for i in range(2,n,2):
    print(i)

for i in range(1, 100, 2):
    print(i, end = ',')

# We can also use the range() function with sequence of numbers.
# The len() function is combined with range() function which iterate through a sequence using indexing.
# Consider the following example.

list = ['Peter','Joseph','Ricky','Devansh']
for i in range(len(list)):
    print("Hello",list[i])
'''
Nested for loop in python
------------------------------------------
Python allows us to nest any number of for loops inside a for loop. 
The inner loop is executed n number of times for every iteration of the outer loop. 
The syntax is given below.

Syntax:

for iterating_var1 in sequence:  #outer loop
    for iterating_var2 in sequence:  #inner loop
        #block of statements
#Other statements
'''
print(" Nested for loop ")
# User input for number of rows
rows = 5
# Outer loop will print number of rows
for i in range(1,rows+1):
# Inner loop will print number of Astrisk
    for j in range(i):
        print("*", end='')
    print()

print(" Program to number pyramid ")
rows = 5

for i in range(0,rows+1):
    for j in range(i):
        print(i,end = '')
    print()


'''
Using else statement with for loop
Unlike other languages like C, C++, or Java, Python allows us to use the else statement 
with the for loop which can be executed only when all the iterations are exhausted. 
Here, we must notice that if the loop contains any of the break statement then the else statement will not be executed.
'''
# Example 1
for i in range(0,5):
    print(i)
else:
    print("for loop completely exhausted, since there is no break.")

# Example 2
for i in range(0,5):
    print(i)
    break
else:print("for loop is exhausted");
print("The loop is broken due to break statement...came out of the loop")


# In the above example, the loop is broken due to the break statement;
# therefore, the else statement will not be executed.
# The statement present immediate next to else block will be executed.

