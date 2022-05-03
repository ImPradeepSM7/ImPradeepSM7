'''
# REQ: so and so......
           1. CRUD :  CREATE RETRIEVE UPDATE DELETE
           2. Datatype/structure
           3. State(variable)
           4. Behavior(Operators, DM, Loops)

'''
x = 10
x = 10.5
is_bool = True
msg = 'Hello World'  # '@!#!@#3213213{}<>?<VCXVEWREWRSDFSDF'

list1 = [1, 1, 2, 3, 4, 5, 6]
print("List data structure :", list1)

'''List properties'''

'''
List properties: [  ,   , ]
==================
# 1. List will allow both homogeneous and heterogenous data
# 2. List allows duplicate elements
# 3. Insertion order maintains
# 4. Follows indexing mechanism while storing elements
# 5. List is mutable   (change)
  
'''

# 1.List will allow both homogeneous and heterogenous data
    # Homo
print("----------Homegeneous---------")
list1 = [1, 1, 2, 3, 4, 5, 6]
print('Integers is list : ', list1)

list1 = [1.5, 3.2, 5.6, 4.8]
print('Float is list   : ', list1)

list1 = [True, False, True, False]
print('Boolean is list : ', list1)

list1 = ['hello', ' world', 'welcome', 'python']
print('Strings is list : ', list1)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Lists   is list : ', list1)

list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('Tuples  is list : ', list1)

list1 = [{1: 1, 2: 2}, {'id': 100, 'name': 'Madhu'}]
print('Dict    is list : ', list1)

list1 = [{1, 2, 3}, {4, 5, 6}]
print('Set is list : ', list1)

    # Hetero
list1 = [100, 14.5, False, 'Hello', [1, 2, 3], (1, 2, 3), {1: 1, 2: 2}, {1, 2, 3}]
print("---Hetero-------", list1)

# 2. List allows duplicate elements
list1 = [10, 10, 20]
print("Duplicates in list : ", list1)

# 3. Insertion order maintains
list1 = [1, 2, 3, 4, 5, 6]
print("Insertion order: ", list1)

# 4. List is mutable
print("----List is MUTABLE-----")
list1 = [12, 22, 13, 54, 35]
      #  0   1    2   3   4
print("Before list : ", list1)
list1[2] = 300
print("After list  : ", list1)

# 5. Follow indexing mechanism
list1 = [12, 22, 13, 54, 35]
      #  0   1    2   3   4



'''
When to use list data structure:
---------------------------------
- Handle group of elements
- Homogeneous/heterogenous, 
- Mutable structures
- With Duplicate values 
'''
print("---------------------- LIST: SEQUENCE OPERATIONS ---------------------")
list1 = [1, 1.5, True, 'HelloWorld', 234]
       # 0   1    2       3           4

'''
seq ops:

1. Indexing
2. Slicing
3. Addition
4. Multiplication
5. check membership
6. length - len()
7. max()
8. min()





'''



# Indexing
print("Indexing : ", list1)
print("Indexing : ", list1[1])
print("Indexing : ", list1[3], list1[-2])
print("Get o in list1 :", list1[3], list1[3][4])

# Slicing
print("Slicing : ", list1)
print("Slicing : ", list1[0:4])

# Adding
print("Adding 2 lists :", [1, 2, 3] + [4, 5, 6])
#Mulitiplying
print("Mulitply 2 lists :", [1, 2, 3] * 2)
# Membership
print("Check value : ", 1 in [1, 2, 3])
# len
print(list1)
print("Length of list1 : ", len(list1))
list2 = [1,2,3,100]
# max
print("max of list1 : ",max(list2))
# min
print("min of list1 : ",min(list2))


list1 = [1, 2, 3, 4, 5]
list2 = [True, False, False]
list3 = ['Hello', 'World', 'python']
list3 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(list3[0][2])


list4 = [(1, 2), (3, 4, 5)]
list5 = [{1: 1, 2: 2}, {1: 'Madhu', 2: 'Nethra'}, {}]
list6 = [{1, 2, 3}, {4, 5, 6}]

print("-----------List3 operations---------")
list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("List3 : ", list3[0])
print("List3 : ", list3[0][1])
print("List3 : ", list3[0:1])
print("List3 : ", list3[1][2])
