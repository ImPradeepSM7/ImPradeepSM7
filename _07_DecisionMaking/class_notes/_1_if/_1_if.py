
'''
Decision Making :
There comes some situation where we need to take some decision ,
on that decision  further execution  of the code depends.

Decision making statements decides the output or result of a program.
In python we can make decision using –

If Statement
If -Else statements if, else
Nested If statements
If-Elif Ladder
Short- Hand if-else statement
Short-Hand If statement


If-Statement :
If statement is the simplest decision making statemet in Python programming.
It is use to decide weather a particular statement is True or not.
If the condition holds true , the statement inside the’IF’ will execute else it will not.

Syntax :

x = 10  (True)
if x = 11 :
    print("x is 10")

if x = 10:
    print(True)

     #statements

#if-statement
=====================
me=‘Prepster’
if(me==‘Prepster’):
    print(‘Welcome to PrepInsta’)
Output :

Welcome to PrepInsta


If-Else Statement :
If we want to do something  else when the condition inside ‘If’ is False , here we use if-else.
If condition holds true , then program will execute the code under the if-condition.
If condition is False , it will execute the code under else part.
Syntax :

  if( condition ):

    #statements

  else:

      #statements
decision making-if-else in-python
#pyhton program
#if-else statement

me=‘Xyz’
if(me==‘Xyzz’):
    print(‘Welcome to PrepInsta’)
else :
    print(‘You are welcome to become a Prepster.’)
Output :

You are welcome to become a Prepster.


Nested If :
Nested if statement means an If statement under another If statement  and Python allows us to do So.
If we have to take some decisions on the basis of two or more condition  we can use nested-if statements.
Synatx :

  if ( condition1):

      #statements

      if(condition2):

          #statements

      #block ends here

  #blocks end here
#pyhton program
#nested if statement
me=‘Xyz’
if(me):
    print(‘Welcome to PrepInsta’)
    if(me==‘Xyz’):
        print(‘You are welcome to become a Prepster.’)
Output :

Welcome to PrepInsta
You are welcome to become a Prepster.
If-elif Ladder :
When we have multiple condition to check and excute according to the given condition , we can use if-elif-ladder.
It’s upto us that we want to use a else portion in the code.
It follows top-down approach.


Syntax :

  if(condition1):

      #statements

elif(condition2):

    #statements

  .

  .

  .

  .

  else:

      #statements

#pyhton program
#if-elif statement
me=”
if(me==‘Prepster’):
    print(‘Welcome to PrepInsta’)

elif(me!=‘PrepSter’ and len(me)>0):
    print(‘You are welcome to become a Prepster.’)
else:
    print(‘You should not be here.’)


Output :

You should not be here.
Short Hand If statement :
Whenever there is only one statement inside the If loop.
The statement can be put on the same line as the if statement.


Syntax :

  if(condition): #statement
Short Hand If -else statement :
Whenever there is only one statement inside the both If-else loop.
The statement can be put on the same line as the if -else statement.
Syntax :

  #staement1 for True  if(condition) else  #statement2 for False.
#pyhton program
#Shirt hand if statement
me=‘Xyz’
if(me==‘Xyz’): print(‘You are welcome to become a Prepster.’)

#Shirt hand if-else statement
me=‘Prepster’
print(‘You are welcome to become a Prepster.’) if(me==‘Xyz’) else print(‘Welcome To PrepInsta’)




Output :

You are welcome to become a Prepster.
Welcome To PrepInsta





'''


# True ==>  1 non-zero non None
# False ==> zero    None
is_active = True
is_perm = False
'''
Water and Coffee
------------------
True and True*   = True
True and False*  = False
False* and True   = False
False* and False  = False
'''
#     F          T     =  F
if 10 > 20 and 10 == 10:
    print("Executed 1")

if 'mani': # not none
    print("Madhu Nettem")

'''
Coffee or Tea:
----------------
True* or True = True
True* or False = True
False or True* = True
False or False* = False

True --> nonZero   except zero          nonNone 
         10 -10 10.4 -3.4     'Hello' [1,2,3] (1,2,3) {1:1,2:2} {1,2,3}

False --> 0                   None 
                              '' [] ()  {} {}


Telugu and Hindi and English
True       True      False    - False
False*  

BTech final semester  2 subjects 

MM or M1 
True*  True      -- True  
True*  False     -- True
False True*       -- True
False False*      -- False 


'''
print("------------------------------------")
#if-statement
name = 'vn2'
if(name==''): # False
    print("if condition fails")
if None:  #False
    print("checking None exec:")
if not None:
    print("checking Not none value : ")

if 'Madhu':  # [1,2,3], (1,2,3), {1:1,2:2}  {1,2,3,4}
    print("Name exec")
if [1,]:  # []  () {}
    print("Empty string")


print("Arithmetic :", 10 + 20)
print("Relational :", 10 >= 20)
print("10 and 20 :", 10 and 20)  # 20 True and True --> True
print("10 and 0  :", 10 and 0)   #  0 True and False --> False
print("0 and 20 :", 0 and 20)    #  0 False and True --> False
print("0 and 0 :", 0 and 0)      #  0 False and False --> False
print("10 or 20 :", 10 or 20)
print("10 or 0 :", 10 or 0)
print("0 or 20 :", 0 or 20)
print("0 or 0 :", 0 or 0)
print("Membership :", 10 in [10, 20, 30])


x = 20
y = 10
if x > y:
    print("X value")

'''
Arithmetic ops: +-*/ // %       ==> 0 / nonzero 
Relational ops: > >= < <= == != ==> True/False
Assignment ops:                     x = 10  x = -10.4
                                    x = 0   x = None
Logical  ops   :                ==> True/False
Bitwise       :                 ==> 0 or 1   False/True
Membership    : in not in       ==> True/False
Identity      : is is not       ==> True/False

'''

'''
1. Single condition     : 1 ==> if 


2. Multiple conditions  : 2 ==> if else
                          3 ==> if elif else            # if   else if    else 
                          4 ==> if elif elif else
                          5 ==> if elif elif elif else

3. nested conditions    : nested if 

                10th exam   
                -----------
L1:            1. PASS                            2. FAIL    if-else
L2:         1.continue     2. disc.           1. retry    2. stop 
L3:    1.Inter   2.Diploma        
L4:  1.MPC  2. BiPC
L5:        1.Govt  2.Pvt

'''
'''
SDLC Process:
-------------
S1 : REQUIREMENT : If user entered value is 20, 
                   then print  "Welcome to Python World" message

S2: ANALYSIS :   Functional Analysis
                 Technical Analysis # if , else

S3: DESIGN: 
            Step1 : Take the user input
            Step2 : Compare the user(customer) provided input with given value(20)
            Step3 : If True, print the message "Welcome to Python World"

S4 : Development
S5 : Testing
S6 : Deployment
'''
print("----------if---------------")
# S4: DEVELOPMENT      # Business logic implementation


#SDLC
x = 10 # static way of input
user_input = int(input("Enter number: "))  # S1 #dynamic way
if user_input == 20:                       # S2
    print("Welcome to Python World")  # S3
print("--------------------------------")
# S5 : Testing
'''
        Positive scenario  : 20  
        Negative scenario  : 15 25 0 -5 0 -20
'''

'''
Condition : Success ==> True  nonZero nonNone
            Failure ==> False Zero    None
 True    / False 
 Non 0   / 0  
 nonNone / None
1. Single condition : if 
'''
# arithmetic
if 10+20:  # 30
    print("Successfully executed 10+20")  # Indentation

if True:
    print("True condition")

if False:
    print("False condition")

if not False:
    print("Print False condition")


if True or False:
    print("OR - condition ")

if True and True:
    print("AND - condition")

if 0:
    print("Value 0")
if None:
    print("Value None")
if not 0:
    print("Value 1")
if not None:
    print("Value not None")

if 10-20:
    print("Addition is success")

if 10 > 20:
    print("End of the program")


