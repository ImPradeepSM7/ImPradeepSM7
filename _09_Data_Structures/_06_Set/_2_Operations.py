#{}

s1 = {1}   # Dictionary
print(s1, type(s1))

s1 = set()
print(s1, type(s1))

s1 = set({})
print(s1, type(s1))

print("---------Iterate through set-----------")
s1 = {1, 2, 4, True, 'Hello', 'Python', (1, 2, 3)}
for each in s1:
    print(each)

print("------UPDATE---------")

# Update set data structure
s1 = {1, 4, 5, 7, 2, 6, 3}
print("Before add ----", s1)
s1.add(100)
print("After add -----", s1)

# Remove  the element
s1.discard(5)
print("After discard--", s1)


# Union
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print("Union -----------: ", s1 | s2)
print("Intersection-----: ", s1 & s2)
print("Minus-----: ", s1 - s2)
print("Minus-----: ", s2 - s1)
