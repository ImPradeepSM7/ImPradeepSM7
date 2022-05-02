
print("------Continue---------")
# continue
'''
REQ:  # Numbers between 1 to 1000 which are divisible by 5.
      # If value is also divisible by 10 don't display it.

Tasks: 1. Print between 1 to 100
       2. Find numbers divisible by 5
       3. If same num divisible by 10 don't do anything

'''
for val in range(1, 101):
    if val % 5 == 0:
        if val % 10 == 0:
            continue
        print(val)




'''
break    : 1. Remaining stmts will not be executed
           2. It breaks the loop and come out of it 
           
continue : 1. It will skip remaining stmts, will go to next iteration
pass     :
'''
'''
if True:
    pass

while True:
    pass

for each in range(1,100):
    pass

print("Hello")
'''
# if elif else while for break continue pass

print("-------- Even numbers -------------")
# Print only first 3 even numbers between 1 to 50
counter = 1
for each in range(1,51):
    if each % 2 == 0:
        if counter > 3:
            break
        print(each)
        counter += 1
print("------Both continue break -----")

# Print even numbers.Skip first 3 even numbers and after 7th even number onwards
counter = 1
for each in range(1,51):
    if each % 2 == 0:
        counter += 1
        if counter <= 4:
            continue
        print(each)
        if counter > 7:
            break

# Find even numbers count in list and print it
print("----Even number count---------")
list1 = [3, 5, 20, 6, 8, 2, 7, 3, 1, 6, 2, 6, 8, 4, 2]

count = 0
for val in list1:
    if val % 2 == 0:
        count += 1
        print(val)

print("Total even numers : ",count)


print("----Even number count tuple---------")
tupl1 = (3, 5, 20, 6, 8, 2, 7, 3, 1, 6, 2, 6, 8, 4, 2)

sum = 1
for val in tupl1:
    sum = sum * val  # 0+3 = 3 + 5 = 8
print("Sum of tuple :",sum)