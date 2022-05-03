# CRUD Operations


# 1. CREATE
list1 = [1, 2, 3, 4, 5, 6]


list1 = [1, 2, [30, 40, 50], (11, 22, 33), {1, 2, 3}, {1: 100, 2: 200}]
# 2. RETRIEVE
print('List values1 : ', list1)
print('List values2 : ', list1[2])
print('List values21 : ', list1[2][1])

# 3. UPDATE
list1[1] = 200
print('List values2 : ', list1)

# 4. DELETE
del list1[2][2]
print('List values3 : ', list1)
del list1
#print('List values4 : ', list1)


# copy - shallow copy/ deep copy


list1 = [1,2,4]
list2 = list1.copy()
print(list1, list2)

print("after append")

list1.append(100)
print(list1, list2)

print("after append list2 ")

list2.append(20)
print(list1, list2)
print("deep copy==============")

list1 = list2 # deep copy

list1.append(200)
print(list1, list2)




# shallow copy made changes to original
# deep copy doesn't change original source

from copy import copy, deepcopy
list1 = [1,2,4]
list2 = copy(list1)  # shallow copy

list1.append("mani")
print(list1, list2)



list3 = deepcopy(list1)
list1.append(22)
print(list1, list3)