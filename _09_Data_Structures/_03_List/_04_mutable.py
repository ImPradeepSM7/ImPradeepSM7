# String is immutable
msg = 'Hello'
print("Before string : ", msg)
msg = 'World'
print("After string  : ", msg)


# List is mutable
list1 = [32, 12, 35, 76, 43, 52, 15]
print(id(list1))
list1[2] = 333
print("after update element:", id(list1))


print("Before list :   ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))
list1[1] = 1000
print("After list  : ", list1, id(list1), id(list1[0]), id(list1[1]), id(list1[2]))
