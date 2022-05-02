

list1 = [1, 2, 3, 4, 5]
# Output : Find square of each number  1, 4, 9, 16, 25
'''
  = [1, 2, 3, 4, 5]
  = [1*1, 2*2, 3*3, 4*4, 5*5]
'''
print("-------Square of list----------")
for val in list1:
    print(val ** 2)


print("-------Membership of 2 lists----------")
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 10, 20, 30]

for val in list1:
    if val in list2:
        print("YES : ", val)
    else:
        print("NO  : ", val)

# Print  first 4 numbers  which are divisible by 9 between 1 to 100
print("-----9 series numbers------------")
count = 0
for val in range(1, 101):
    if val % 9 == 0:
        print(val)
        count += 1
        if count == 4:
            break
print("End of loop")
