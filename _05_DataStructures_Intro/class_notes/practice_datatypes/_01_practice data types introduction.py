x = 10
print("DataType is :", type(x))
y = "mani"
print("Data type is :", type(y))
x = "Hello world"
print(type(x))  # string
x = 20
print(type(x))  # int
x = 20.5
print(type(x))  # float
x = 5j
print(type(x))   # complex
y = ("apple", "banana")
print(type(y))        # tuple
y = ["apple", "banana"]
print(type(y))         # list
y = {1, 2, 3, 4, 7, 8}
print(type(y))      # sets
z = {"name": "mani", "age": 26}
print(type(z))                # dictionary
mani = {"emp_id": 596263, "cont_no": 6281651717}
print(type(mani))
brand = {
    "brand": "audi",
    "car year": 2016,
    "model": "x1"
}
print(brand)
print(type(brand))
x = frozenset({"apple", "banana", "cane"})
print(type(x))
x = frozenset({1, 2, 3, 45})
print(type(x))
m = True
print(type(m))
x = range(6)
print(type(x))
x = b"hello"
print(type(x))
# text_type:string
# numeric_type:int,float,complex
# sequence_type:list,tuple,range
# mapping_type:dictionaries
# sets_type:sets,frozenset
# boolean_type:bool
# binary_type:byte,bytearray,memory
x = bytearray(5)
print(type(x))
x = memoryview(bytes(6))
print(type(x))
x = b"welcome"
print(type(x))
y = bytes(5)
print(type(y))
z = bytearray(5)
print(type(z))
m = memoryview(bytes(5))
print(type(m))

# setting_the_specific_data_type
m = str("hello world")
print(m)
print(type(m))
_poem1 = str('''johnny jonny yes papa
eating sugar no papa
telling lies no papa
open your mouth ha ha''')
print(_poem1)
print(type(m))


# int type
x = int(50)
print(x)
print(type(x))

y = int(200)
print(y)
print(type(y))

z = int(152.326)
print(z)
print(type(z))


# float type

d = 52.26
print(type(d))
a = float(5263.289)
print(type(a))
print(a)


# complex_type

x = complex(1j)
print(x)
print(type(x))

# Tuple type

a = tuple(("water", "tea", "coffee"))
print(a)
print(type(a))

w = ("water", "tea", "coffee")
print(w)
print(type(w))

# list type

r = list(("apple", "tree", "cart"))
print(r)
print(type(r))

s = list(("bag", "ball", "cat", 1, 2, 3))
print(s)
print(type(s))

# set type

x = set((1, 2, 3, 4, 5))
print(x)
print(type(x))

x = set(("mani", "jyo", "bharat"))
print(x)
print(type(x))

# dict type

x = dict(name="john", age=26)
print(x)
print(type(x))

r = dict(shape="circle", planetype="flat")
print(r)
print(type(r))

# bool type

p = True
print(p)
print(type(p))

q = False
print(q)
print(type(q))

# Byte type

e = bytes(6)
print(e)
print(type(e))

r = bytes(8)
print(r)
print(type(r))

# memory view
s = memoryview(bytes(5))
print(s)
print(type(s))

d = memoryview(bytes(5))
print(d)
print(type(d))

# bytearray type

f = bytearray(8)
print(f)
print(type(f))

c = bytearray(1)
print(c)
print(type(c))
