'''

len()
count()
index()
'''

list1 = [1, 2, 3, 4]
print("Before : ", list1, type(list1))
tup1 = tuple(list1)
print("After : ", tup1, type(tup1))


t1 = (10, 43, 2, 532, 53, 64, 24, 25, 53)
print("Iterate the tuple")
for each in t1:
    print(each)

le = len(t1) # 9 elements
for i in range(len(t1)):  # range(9) 0123456789
    print(i, " : ", t1[i])


# Find index of 64
t1 = (10, 43, 2, 532, 53, 64, 24, 25, 24, 10,  53, 10)
print("length of t1",len(t1))

for i in range(len(t1)):  # lengrh - 12 range(12)
    if t1[i] == 64:
        print("Index is : ", i)

print("Count : ", t1.count(10))

print("Index : ", t1.index(64))  # print(t1[5])


list1 = [1, 2, 3]
print("Before : ", list1)
list1.append(10)
print("After  : ", list1)
# return type

# pop() remove()
print("List pop :", list1.pop(2))  # index position
print(list1)
print("List remove :", list1.remove(10))  # value
print(list1)


tup1 = (1,4,[2,3])
tup1[2].append(100)
print(tup1)