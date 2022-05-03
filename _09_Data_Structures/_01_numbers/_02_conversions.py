'''   1234*  1234%   999*000   *123
Type conversions
-----------------
int()
float()
complex()
bool()
--------
str()
list()
tuple()
dict()
set()


'''

sal = 1000
print("Salary : ", sal, type(sal))

sal = float(sal)
print("Salary : ", sal, type(sal))

m_bill = 234.45
print(m_bill, int(m_bill))
print("Mobile bill : ", m_bill, type(m_bill))
mobile_bill = int(m_bill)
print("Mobile bill : ", m_bill, type(m_bill))


# Boolean
# True nonZero non None
# False 0 None
x = 0
print("Normal val : ", x, type(x))
x = bool(0)
print("Boolean val : ", x, type(x))

y = 1
print("Normal val : ", y, type(y))
x = bool(y)
print("Boolean val : ", x, type(x))

x = 232
x = bool(-232)
print("Boolean value : ", x, type(x))