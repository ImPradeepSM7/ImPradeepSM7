'''
An array is a data structure that can contain or hold a fixed number of elements
that are of the same Python data type.
An array is composed of an element and an index.
Index in an array is the location where an element resides.
All elements have their respective indices. Index of an array always starts with 0.
'''

'''
ARRAYS: [] or array([])
----------
 - Allows homogenous data only
 - Are used to store multiple values in single variable 
 - An array is a collection of items stored at contiguous memory locations.


# diff b/w list and array
  list                                   array
1. heterogenous data                  1. homogenous data
2. memory efficiency is low           2. memory efficiency is good  
'''

import array as arr
# from array import *


my_arr = arr.array('i',[12, 32, 43])  # Only Homogeneous data
print(my_arr, type(my_arr))

print("-------Iterate through each value-----")
for each in my_arr:
    print(each)

print("-------Iterate through each index-----")
for ind in range(len(my_arr)):
    print(my_arr[ind])

# Adding elements to array
my_arr.insert(1, 100)
print("After inserting : ", my_arr)

# Retrieve elements from array
print("Array elements : ", my_arr)
print("Array elements : ", my_arr[0])
print("Array elements : ", my_arr[1:2])


# https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/

'''
list1 = [1,2,3]
print("List add : "list * 5)   # Array ==> [1,10,15]


'''

array = [1,10]
print(type(array), array)