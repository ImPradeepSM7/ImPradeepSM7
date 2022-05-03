
# Conversions
x = 10
print("To float : ", float(x), type(x))
x = 10.5
print("To int  : ", int(x), type(x))
x = 0
print("To bool : ", bool(x), type(x))
x = -5
print("To bool : ", bool(x), type(x))

x = 12345
print("To str  : ", x, type(x))
x = str(x)
print("To str  : ", x, type(x))


str1 = 'Hello World'
print("Convert to list : ", list(str1))


list1 = [1, 2, 3, 4, 5, 6]
print("List to string : ", list1, type(list1))
st = str(list1)
print("List to string : ", st, type(st))  # "[1, 2, 3, 4, 5, 6]"
'''
[1, 2, 3,  4 ,  5 ,   6]
012345678910 11 121314 15
'''
list1 = ['a', 'b', 'c']
num_str = '10'.join(list1)
print(num_str, type(num_str))
num_str = ' '.join(list1)
print(num_str, type(num_str))
