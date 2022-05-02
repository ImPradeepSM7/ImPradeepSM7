

x = 10
print(x, type(x), id(x))

msg = 'Hello World'
'''
    H e l l o   W o r l  d 
    0 1 2 3 4 5 6 7 8 9 10
                   -3-2 -1
213213213
'''
print(msg)
print("4th index :", msg[4])
print("10th index :", msg[10])
print("10th index :", msg[-1])
print(id(msg))
print(id(msg[2]), id(msg[5]))



'''
Python will load RHS, first it will prepare indexing mechanism for each character in string
H e l l o   W o r l d
0 1 2 3 4 5 6 7 8 9 10

00001110 01110010 01110010 01110010 01110010 01110010 01110010 01110010 01110010

'''

x = 10
print("Value of x: ", x)
x = 20
print("Value of x: ", x)

msg = 'Hello World'
print("Message1 is : ", msg, id(msg))

msg = 'Python'
print("Message1 is : ", msg, id(msg))



x = 10
x = x + 20

msg = 'hello'  # immutable fixed
print('Message2 : ',msg)
msg = 'Hello' + 'world'
print('Message2 : ',msg)


x = 'Hello World'
x = [1,2,3,4,5,6,7,8]
for x[-1] in x:
    print(x[-1])
