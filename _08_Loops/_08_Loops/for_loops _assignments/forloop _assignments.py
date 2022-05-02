
print("sum and average of user input number until zero")

num = 1
i = -1
s = 0
while(num!=0):
    num = int(input("enter any number"))
    s = s + num
    i = i + 1  # (here i +)
print("sum of numbers entered by user", s)
print("Average of numbers entered by user", s/i)



