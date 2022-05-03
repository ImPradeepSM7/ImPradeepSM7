x = 10  # write operation  CREATE
print(x)  # read operation  RETRIEVAL/READ
print(20)
print(10+20)

'''
list1 = [ , ]
A Tuple is a collection of Python objects separated by commas. (, , )
In someways a tuple is similar to a list in terms of 
indexing, nested objects and repetition 
but a tuple is immutable unlike lists which are mutable.
Difference Between List and Tuple in Python:  

SR.NO.	LIST	                                          TUPLE

1	Lists are mutable	    lst = [1,2,5] pop      1. Tuples are immutable
2	Implication of iterations is Time-consuming	   2.The implication of iterations is comparatively Faster
3	The list is better for performing operations,  3.Tuple data type is appropriate for accessing the elements
    such as insertion and deletion.
4	Lists consume more memory	                   4.Tuple consume less memory as compared to the list
5	Lists have several built-in methods	           5.Tuple does not have many built-in methods.
6	The unexpected changes and errors are more     6.In tuple, it is hard to take place
    likely to occur

for i in lst:
    print i



'''



li1 = [1, 2, 3, 4]     # Mutable
tup1 = (1, 2, 3, 4)    # Immutable
print(tup1, type(tup1))
x = tup1.index(1)
y = li1.append(12)
print("index position of x:", x)
tup1 = ()
print("Empty tuple :", tup1, type(tup1))

tup1 = ('a',)
print("Empty tuple :", tup1, type(tup1))

tup1 = (1,)
print("Empty tuple :", tup1, type(tup1))


'''
tuple to list  tup2 = list(tup1)
perform methods x = tup2.append()
result convert into tuple res = tup(x)
'''
str ="hello world"  #  elemnts
lst = [13, 67, 98]
tup = (22, 24, 67)

for i in str:   # iterations
    print(i)

for each in lst:
    print(each)

for ele in tup:
    print(ele)


for num in range(0, 100, 5):
    print(num)