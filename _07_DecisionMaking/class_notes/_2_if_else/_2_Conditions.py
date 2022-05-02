# Find the value of X2+2x+1 when x is 10
'''
# STATE
As given x = 10
# BEHAVIOR
Substitute value of x in given expression
 = x2+2x+1
 = (10)2+2(10)+2
 = 100+20+2
 = 122


'''
'''
# REQUIREMENT : Get student result(Pass/Fail) based on given input marks.
    User criteria: 
    --------------
    If marks are greater than or equal to 35 then display as PASS else FAIL
                    >= 35 --> PASS
                    < 35  --> FAIL  
                    DecisionMaking(if else)
    Conditions: 
    ------------
    customer input data should not be greater than 100 and less than 0 
'''

'''
Step1 : STATE    : Datatype/Datastructure (int/float/bool/string/list/tuple/dict/set)
Step2 : BEHAVIOR : Business Logic implementation

STATE       : S1: int : marks   
BEHAVIOR    : S2: Decision Making concept   (Get student result(Pass/Fail))
Validation  : DecisionMaking
'''
print("-----------Result with PASS/FAIL-----------")
    # 1. STATE
# marks = 80  # static way of data initialization,  hardcoding data
marks = int(input("Enter marks b/w 0 to 100 :"))   # Dynamic way

    # 2. B    EHAVIOR
if marks >= 0 and marks <= 100:   # 0 to 100
    if marks >= 35:  # True
        print(marks, "Result : PASS")
    else:
        print(marks,"Result : FAIL")
else:
    print("Please enter valid marks")

marks = int(input("Enter marks :"))   # Dynamic way
# 2. BEHAVIOR
if marks < 0 or marks > 100:
    print("Please enter valid marks")
else:
    if marks >= 35:
        print("Result : PASS")
    else:
        print("Result : FAIL")




'''
Testcases :     65, 25, 0, 100,  35,34,36


'''
# validation logic : customer input data should not be greater than 100 and less than 0



'''
REQ: Check whether given number is - positive or 
                                   - negative
                                   - neither positive nor negative
1 condition  : if 
2 conditions : if else
3 conditions : if elif else
4 conditions : if elif elif else
5 conditions : if elif elif elif else
'''
print("-----------Positive or Negative-----------")
#num = 10
num = int(input("Enter any number: "))

if num > 0:
    print("Number is positive")
elif num < 0:  # -1  , 0
    print("Number is negative")
else:     # elif num == 0
    print("Neither pos. nor Neg.")



'''
Find Student result for input marks with class category. 
                    First class  >= 60
                    Second class >= 50 and < 60
                    Third class  >= 35 and < 50
                    Fail         <  35
Add validation logic for wrong input data 
'''
print("-----------Result with class-----------")
# STATE
marks = int(input("Enter marks :"))

# BEHAVIOR
 # 1. Validation
if marks < 0 or marks > 100:
    print("Please enter valid marks between 0 to 100")
else:
    if marks >= 60:
        print("Result : FIRST CLASS")
        if marks == 100:
            print("-----SUPER..Congratulations-----")
        elif marks >= 90:
            print("----GOOD..Congratulations-------")
    elif marks >= 50 and marks < 60:
        print("Result: SECOND CLASS")
    elif marks >= 35 and marks < 50:
        print("Result: THIRD CLASS")
    else:
        print("Result: FAIL")
        if marks == 0:
            print("--------DOUBLE SUPER----------")