'''
set is mutable, where elements are immutable. It follows hashing algorithm

'''
# Example
s1 = {1, 2, 2, 2, 2, 4, 3, 5, 2, 7, 6}
print("Set 1 : ", s1)
# s1 = {[1, 2, 3]}
# s1 = {{'eid': 100, 'name': 'Madhu'}}
# s1 = {1, 2, 3, {1, 2, 3}}

# Immutable : Elements inside set are Immutables
# Set is mutable stucture

s1 = {1, 1, 3, True, 'Hello', (1, 2, 3)}
# s1[1] = 3   # won't works here it follows  hashing not indexing
# TypeError: 'set' object does not support item assignment
print("Set is Mutable : ", s1)
s1 = {{1, 2, 3}, {1: 1, 2: 2}, [1, 2, 3]}

# It doesn't follow indexing. It follows hashing algorithm
