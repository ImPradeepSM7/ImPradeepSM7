# strings
var_1 = "hello world"
var_2 = " python executes"
print(var_1[2])
print(var_1[5:9])
print("variable value is :", (var_1 + var_2))
print(var_2[6])
print(var_2[1:8])
# update_string
print(var_1[:5] + " boom")
# del var_1
print(var_1)

# lists
list1 = [1, 2, 5, 6, 8, 9]
list2 = ['axe', "ant", "apple"]
print(list1)
print(list2[0:5])
print(list1[0:5])
print(list2)
mylist = ["apple", "banana", "cane"]
print(mylist)
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])
print(mylist[0])
print(mylist[1])
print(mylist[2])
print("value at first index is :", mylist[1:2])
thislist = ["apple", "orange", "mango", "berry", "guava"]
print(thislist[2:5])
print(thislist[-4:-1])
print(thislist[3])
thislist[1]="blackcurrent"
print(thislist)

# tuples
tup1 = ("apple", "water", "cake", "tea")
print(tup1)
print(tup1[3])
print(tup1[-2])
print(tup1[-3:-1])
print(tup1[0:4])
k = ("den",)
tup1 += k
print(tup1)
m = ("paper",)
tup1 += m

print(tup1)
# sets
set1 = {"paper", "pen", "gum"}
print(set1)
print(len(set1))
set2 = {1, 2, 3, 4, 5, 6}
set3 = {True, False, False}
for u in set1:
    print(u)
print("pen" in set1)
set1.add("pencil")
print(set1)
set1.update(set2)
print(set1)
set1.update(set3)
print(set1)
list = ["fan", "movie", "camera"]
set1.update(list)
print(set1)

set1.remove("fan")
print(set1)

# dictionaries
dict = {"car" :"benz",
        "year":2016,
        "brand":"ford"}





