for i in reversed(range(2,21,2)):
    print(i)

print("*"*20)

for i in reversed(range(1,5)):
    print(i*"#")

print("*"*20)

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print("*"*20)
# multiplication table
n=int(input("enter a no:-"))
for i in range(1,11):
    m=n*i
    print("multiplication table is {} X {} = {}".format(n,i,m))

print("*"*20)
# Factorial
num = int(input("enter a number:= "))
fact=1
if num<0:
    print("sorry,number doesn't exist: ")
elif num==0:
    print("factorial number is 1: ")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial number of",num,"is",fact)

print("*"*20)
# Prime no
num = int(input("enter a number:"))
for i in range(2,num):
    if num % i == 0:
        print("it is not a prime nummber: ")
        break
else:
    print("it is a prime number: ")

print("*"*20)

# pattern

for i in range(5, 0, -1):
    for j in range(0, i):
        print(i, end="")
    print()

print("*"*20)

# ABCD Pattern
k = 64;
for i in range(69, 64, -1):
    for j in range(i, 70):
        k += 1
        a = chr(k)
        print(a , end=" ")
    print()

print("*"*20)
# Sum of the number
n= int(input("Enter a no:- "))
s=0
for i in str(n):
    s=s+int(i)
print("sum of the digits = {}".format(s))

print("*"*20)

# Product of the number
n= int(input("Enter a no:- "))
m=1
for i in str(n):
    m=m*int(i)
print("Product of the digits = {}".format(m))

print("*"*20)

# Print numbers from 1 to 20 except multiple of 2 & 3 ?
for i in range(1,21):
    if (i%2 != 0) and (i%3 !=0):
        print(i)

print("*"*20)

# Even and Odd sum between 12 to 37
es=0
os=0
for i in range(12,38):
    if(i%2==0):
        es=es+i
    else:
        os=os+i
print("Sum of even number = {}".format(es))
print("Sum of odd number = {}".format(os))

print("*"*20)

# Write a program to display all the numbers which are divisible by 11 but not by 2 in between 100 to 500 ?
for i in range(100,501):
    if (i%11 == 0) and (i%2 !=0):
        print(i)

print("*"*20)

# White a program that keep on accepting number form the user until user enters zero. Display the sum and average of all the numbers.
print("Input some numbers. input 0 to exit:=.")
sum=0
num=1
i=0
while num!=0:
        num = int(input("enter a number"))
        sum=sum+num
        i=i+1
if i==0:
    print("put numbwe")
else:
    print("Average and sum of the number are:",sum/i,sum)

print("*"*20)

print("input numbers:=  . input 0 exit")
s= 0
i=0
n=1
while (n!=0):
    n= int(input("enter the number: "))
    s= s+n
    i= i+1

avg = s/i
print(s)
print(avg)

print("*"*20)