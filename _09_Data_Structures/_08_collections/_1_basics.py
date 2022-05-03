'''
builtins.py
----------
print()
id()
type()
int() float() complex() bool()
str() list() tuple() dict() set()
40    10     3       10     3

#include<stdio.h>
#include<conio.h>
#include<math.h>

c program :
5 line             505 lines
.c --> compile --> .obj
'''
list1 = list()
list1.append(100)
list1.append(200)
list1.append(300)
print("List data structure: ", list1)  # from builtins module


from collections import *

d1 = OrderedDict({1: 1, 3: 3, 2: 2})
print("Order dictionary : ", d1)


x=10
x = 10
list1 = [1,2,3,4]


'''
This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.

namedtuple():
-------------------

factory function for creating tuple subclasses with named fields

deque:
---------------

list-like container with fast appends and pops on either end

ChainMap:
--------------------

dict-like class for creating a single view of multiple mappings

Counter:
-------------------

dict subclass for counting hashable objects

OrderedDict:
----------------------

dict subclass that remembers the order entries were added

defaultdict:
------------

dict subclass that calls a factory function to supply missing values

UserDict:
---------------

wrapper around dictionary objects for easier dict subclassing

UserList:
-------------
wrapper around list objects for easier list subclassing

UserString:
----------------------

wrapper around string objects for easier string subclassing

'''