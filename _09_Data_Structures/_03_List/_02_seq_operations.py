list1 = [12, 22, 13, 54, 35, 76, 14]
print("List1 : ", list1)

# 1. Sequence operations

print("----------1. Indexing-------------")
'''                                                                     
    [12, 22, 13, 54, 35, 76, 14]   1 2 3 4 5 6 7 8 9 10 
      0  1   2   3   4   5   6    
'''
print("List1 1    : ", list1[1])
print("List1 5,-1 : ", list1[5], list1[6], list1[-1])

print("----------2. Slicing-------------")
print("Slicing operation : ", list1[2:])
print("Slicing operation : ", list1[2:5])
print("Slicing operation : ", list1[:5])
print("Slicing operation : ", list1[::1])
print("Slicing operation : ", list1[::2])

print("----------3. Adding-------------")
print("Adding 2 lists    :", [1, 2, 3] + [4, 5, 6])  # print(10+20) [1,2,3,4,5,6]
list1 = [10, 20, 30]
list2 = [11, 12, 13]
print("Adding 2 lists    :", list2+list2)   # x=10 y= 20   print(x+y)


print("----------4. Multiplying-------------")
print("Multiply 2 lists :", [1, 2, 3] * 5)

print("----------5. Membership-------------")
print("Check value : ", 1 in [1, 2, 3])
print("Check value : ", 10 in list1)

print("----------6. length-------------")
print("Length of list1 : ", len(list1))

print("----------7. max-------------")
print("Length of list1 : ", max(list1))

print("----------8. min-------------")
print("Length of list1 : ", min(list1))
