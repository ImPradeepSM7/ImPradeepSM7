is_active = True
print("Are you active ??", is_active, type(is_active))

x = 0
print(x, type(x))
x = bool(0)
print(x, type(x))


x = None
print(x, type(x))
x = False
print(x, type(x))

'''
if False -->  False
if None  -->  False
if 0     -->  False 
    
if True    --> True
if not None -> True
if -5      -->  True
'''