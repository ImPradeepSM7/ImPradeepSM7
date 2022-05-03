'''list1=[{1:1,2:2},{'id':100,'name': 'madhu'}]
print("dict is list :",list1)

list1=[{1,2,3},{4,5,6}]
print("set is list :-",list1)

list1 = [10, 10, 20]
print("Duplicates in list : ", list1)

list1 = [12, 22, 13, 54, 46]
print(list1)
list1[2] = 300
print(list1)
print("indexing : ", list1[1])
print()

list1 = ['a', 'b', 'c', 'd']
num_str = '10'.join(list1)
print(num_str, type(num_str))
num_str = ' '.join(list1)
print(num_str, type(num_str))

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

list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before pop   : ", list1)
list1.pop(3)  # index
print("After  pop   : ", list1)  # [23, 12, 46, 14, 7, 2, 19, 25]
print(list1.pop())
print("After  pop   : ", list1)  # [23, 12, 46, 14, 7, 2, 19]

list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before removal : ", list1)
list1.remove(34)
print("After removal  : ", list1)

list1 = [23, 14, 12, 46, 34, 14, 7, 2, 14, 19, 25]
print("Before removal : ", list1)
list1.remove(14)
list1.pop(5)
print("After removal  : ",list1)

list1 = [1, 2, 3, 4, 5]
print("Before copy list1    : ", list1)
list2 = list1.copy() # individual copy
print("After copy list2     : ", list2)
print("Normal copy function : ", id(list1), id(list2))
list1.append(100)

print("After append : list1 :", list1)
print("After append : list2 :", list2)

# 2nd way of copy

list1 = [1, 2, 3, 4, 5]
list2 = list1
print("Variable  copy : ", id(list1),id(list2))
list1.append(100)
print("After var copy :", list1,list2)
list2.extend([11,22])
print("After var copy :", list1,list2)

li1 = [1, 2, 3, 4]     # Mutable
tup1 = (1, 2, 3, 4)    # Immutable
print(tup1, type(tup1))
x = tup1.index(1)
y = li1.append(12)
print("index position of x:", x)
tup1 = ()
print("Empty tuple :", tup1, type(tup1))

tup1 = ('a',)
print("Empty tuple :", tup1, type(tup1))

tup1 = (1,)
print("Empty tuple :", tup1, type(tup1))

t1 = (10, 43, 2, 532, 53, 64, 24, 25, 24, 10,  53, 10)
print("length of t1",len(t1))

for i in range(len(t1)):  # lengrh - 12 range(12)
    if t1[i] == 64:
        print("Index is : ", i)

print("Count : ", t1.count(10))

print("Index : ", t1.index(64))  # print(t1[5])

data = {1: 'One', 2: 'Two', 3: 'Three', 'id': '100'}

# RETRIEVE
print("Dictionary : ", data, type(data))
print("Dict item  :", data[2])
print("Dict item  :", data['id'])'''

'''from array import *
vals = array('i', [2, 3, 5, 6, 9, 7])
newArr = array( vals.typecode,(a*a for a in vals))

for p in newArr:
    print(p)'''

from array import *
arr = array('i', [])
n = int(input("enter the length of the array:- "))

for i in range(n):
    x = int(input("Enter the elements of array:- "))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search:- "))
print(arr.index(val))