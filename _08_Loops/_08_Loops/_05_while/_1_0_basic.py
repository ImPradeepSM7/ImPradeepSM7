
'''

The while loop in Python is used to iterate over a block of code as long as
the test expression (condition) is true.

We generally use this loop when we don't know the number of times to iterate in advance

In the while loop, test expression is checked first.
The body of the loop is entered only if the test_expression evaluates to True.
After one iteration, the test expression is checked again.
This process continues until the test_expression evaluates to False.

In Python, the body of the while loop is determined through indentation.

The body starts with indentation and the first unindented line marks the end.

Python interprets any non-zero value as True. None and 0 are interpreted as False

'''


# I REQ. Gathering : Print numbers from 100 to 200

# Code duplication,we can't extend when requirement changes
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

#print numbers from 1 to 5
'''
while <condition>:
    <statements body> 
'''
print("--------------")
x = 1
while x <= 5:
    print(x)
    x += 1   # Assignment operator += -=   x += 1
print("End of program")
'''
1. Data initialization     x = 1
2. Condition verification  while x <= 5
3. Business logic          print(x)
4. Data operation          x = x + 1
'''

print("--------------")



'''
# II - ANALYSIS
        1. Functional analysis : We need to print the numbers between starting and 
                                 ending number given by customer
        2. Technical analysis  : STATE    :  input: st_num end_num (int)
                                 BEHAVIOR :  Loops : while  
III.  Design : NA
'''
# IV. DEVELOPMENT
    #STATE
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
    #BEHAVIOR
while num1 <= num2:
    print(num1)
    num1 += 1
print("***** End of program *****")

# V. TESTING validation is missing

num1 = 500
num2 = 100
if num1 <= num2:
    while num1 <= num2:
        print(num1)
        num1 += 1
else:
    print("### num1 should be less than num2  ###")
print("***** End of program *****")





# Program to add natural
# numbers up to
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = 10

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


# SDLC, STLC

'''
1. Requirement
2. Analysis FA, TA
3. DEsign
4. DEvelopment BL
5. Testing 
6. Deployment

'''