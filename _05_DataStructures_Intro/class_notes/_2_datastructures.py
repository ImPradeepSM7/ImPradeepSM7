# indexing: To retrieve specific element through usig index position
# indexing returns/retrieve single element

#slicing: To get a piece of elements,partial string/data


print("------------STRING------------")
name = 'Madhu Nettem'
# 0123456789   0 to n-1
#  -n          -3-2-1   negative indexing
print(name)
print("0th index value  : ", name[0])   # indexing
print("6th index value  : ", name[6])
print("5th negative index value  : ", name[-5])
print("Get partial name : ", name[0:7])  # slicing  (start value to end-1 value)
print("get reverse string using -ve indexing:", name[::-1])
print(name[-7:-1])



office = "Oracle India Pvt Ltd"
print(office)

# List
print("------------LIST------------")

list1 = [110, 23.5, True, 'Madhu', [1,2,3], (1,2), {1:10,2:20}, {1,2,3}]
print("List1 : ", id(list1))
print("Index 3rd  : ", id(list1[3]))    # Indexing
print("Index : ", id(list1[3][1]))    # Indexing
print("Slice : ", list1[3][1:3])  # Slicing

# Tuple
print("------------TUPLE------------")

tup1 = (110, 23.5, True, 'Madhua', [1,2,3], (1,2), {1:10,2:20}, {1,2,3})
print("Tuple : ", tup1)
print("Index : ", tup1[3])    # Indexing
print("Index : ", id(tup1[3][1]) , id(tup1[3][-1]))   # Indexing


print("------------DICTIONARY------------")

e_data = {'eid': 100,
          'name': 'MadhuNettem',
          'sal': 15000,
          'loc': 'Bangalore',
          'gender': 'Male'
          }

print("Dict data : ", e_data)
print("Dict data : ", e_data['name'])
print("Dict data : ", e_data['sal'])


print("------------SET------------")

set1 = {1, 2, 3, 4, 5, 6}
print("Set1 : ", set1)

print([1,2,2]*-2)
import  pandas as  pd
df1 = pd.DataFrame([1,2])
df = df1
if id(df1) == id(df):
    print("yes", id(df1))
else:
    print("no")
