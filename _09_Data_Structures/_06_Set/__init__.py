'''
Mathematically a set is a collection of items not in any particular order.
A Python set is similar to this mathematical definition with below additional conditions.
# properties of python set:

1.The elements in the set cannot be duplicates.
2.The elements in the set are immutable(cannot be modified)
but the set as a whole is mutable.
3.There is no index attached to any element in a python set.
So they do not support any indexing or slicing operation.

List properties:
==================
# 1. List will allow both homogeneous and heterogenous data
# 2. List allows duplicate elements
# 3. Insertion order maintains
# 4. Follows indexing mechanism while storing elements
# 5. List is mutable

Tuple properties: ()
======================
1. A tuple is a sequence of immutable Python objects.
2. Tuples are sequences, just like lists.
3.The differences between tuples and lists are, the tuples cannot be changed
unlike lists and tuples use parentheses, whereas lists use square brackets.


Dictionary properties: {}
=================================
1. Keys are unique within a dictionary.
2. The values of a dictionary can be of any type,
but the keys must be of an immutable data type such as strings, numbers, or tuples
3. duplicate keys not allowed

Set Operations
The sets in python are typically used for mathematical operations like
1.union,
2.intersection,
3.difference and
4.complement etc.
We can create a set, access it’s elements and carry out
these mathematical operations as shown below.
'''

# Creating a set
# A set is created by using the set() function or placing all the elements
# within a pair of curly braces.


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])  #int(), float()
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)

# Accessing Values in a Set
# We cannot access individual values in a set.
# We can only access all the elements together as shown above.
# But we can also get a list of individual elements by looping through the set.

# Example
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

for d in Days:
   print(d)

# Adding Items to a Set
# We can add elements to a set by using add() method.
# Again as discussed there is no specific index attached to the newly added element.

Days = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat"}
Days.add("Sun")
print("after adding: ", Days)




# Removing Item from a Set
# We can remove elements from a set by using discard() method.
# Again as discussed there is no specific index attached to the newly added element.

# Example
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Days.discard(" ")
print("after discard:", Days)

# Union of Sets
# The union operation on two sets produces a new set containing
# all the distinct elements from both the sets.
# In the below example the element “Wed” is present in both the sets.

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print("after union of sets", AllDays)




# Intersection of Sets
# The intersection operation on two sets produces a new set containing only
# the common elements from both the sets.
# In the below example the element “Wed” is present in both the sets.

DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print("intersection of sets: ",AllDays)

# Difference of Sets
# The difference operation on two sets produces a new set containing only
# the elements from the first set and none from the second set.
# In the below example the element “Wed” is present in both the sets so
# it will not be found in the result set.
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB # DaysB - DaysA

print("difference of sets: ", AllDays)

# Compare Sets
# We can check if a given set is a subset or superset of another set. 'C'
# The result is True or False depending on the elements present in the sets.

# Example
setA = set(["Mon","Tue","Wed"])
setB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = setA <= setB  # a set of which all the elements are contained in another set.
SupersetRes = setB >= setA  # a set which includes another set or sets.
print("setA is subset of setB: ", SubsetRes)
print("setB is superset of setA: ", SupersetRes)


