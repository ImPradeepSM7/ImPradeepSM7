# addition1.py
# This porogram computes addition of two values by using Functions

def sumop(a, b):
    c = a + b
    return c


# main program
k = float(input("Enter First Value:-"))
v = float(input("Enter Second Value:-"))
res = sumop(k, v)
print("Sum={}".format(res))
