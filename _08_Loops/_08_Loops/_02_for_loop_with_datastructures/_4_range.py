print("--------For loop with range-------")
'''
Range:   single value:  (end_val+1)                -  100     - 0,1,2,3..99
         two values  : (st_val, end_val+1)         - (100,201)  --> 1,2,3..20
         three values: (st_val, end_val+1, diff)   - (5,101,6) --> 5,11,17,23..
'''
# here range is special function
'''
10 ==> 0-9
5  ==> 0-4

'''
print("----10------")
for val in range(10):  # 0 to 9
    print("Range val : ", val)
print("----5------")
for val in range(5):   # 0 to 4
    print("Range val : ", val)
print("-----0-----")
for val in range(0):
    print("Range val : ", val)
print("-----1-----")
for val in range(1):
    print("Range val : ", val)

print("----15 to 47----")
for val in range(15, 48):  # 15 to 47
    print("Range val: ", val)

print("----1 to 15----")   # 1 to 15
for val in range(1, 16):
    print("Range val: ", val)


print("----1 to 15 difference with 2----")
for val in range(1, 16, 2):
    print("Range val: ", val)


print("----1 to 30 difference with 3----")
for val in range(1, 31, 3):
    print("Range val: ", val)


print("-----Range with negative---------")
for val in range(20, 1, -1):
    print("Range val: ", val)

print("------ -20 to -40  1-------")
for val in range(-20, -40):
    print("Range val: ", val)

print("------ -20 to -40-------")
for val in range(-20, -40, -1):
    print("Range val: ", val)
