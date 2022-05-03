'''

keys
values
items
update
copy
clear to remove all data
from_keys [10, ] assign same value
has_key
pop
popitem
set_default



'''





# len()
e_data = {'eid': 100,
          'name': 'MadhuN',
          'sal': 14000,
          'mobile': '7406900500',
          'office': 'Bangalore'
          }

print("Length of dict : ", len(e_data))

# type()
print("Length of dict : ", type(e_data))

# str()
di_str = str(e_data)
print("Dict in string format :", type(di_str), di_str)

# dict()
# di2 = dict({})


# Builtin functions:
#=======================
e_data = {'eid': 100,
          'name': 'MadhuN',
          'sal': 14000,
          'mobile': '7406900500',
          'office': 'Bangalore'
          }

# 1. keys() :To retrieve all keys from dictionary
print("-----------1. KEYS----------")
d_keys = e_data.keys()
print("E Data keys : ", d_keys, type(d_keys))
d_keys = list(e_data.keys())  # ['eid', 'name', 'sal', 'mobile', 'office']
print("E Data keys : ", d_keys, type(d_keys))

print("-----Dictionary keys ------")
for key in e_data.keys():   # list(e_data.keys())
    print(key)

print("-----------2. values()----------")
# values() : To retrieve all values from dictionary
d_vals = e_data.values()
print("E Data values :", d_vals, type(d_vals))
d_vals = list(d_vals)  # [100, 'MadhuN', 14000, '7406900500', 'Bangalore']
print("E Data values :", d_vals, type(d_vals))

print("-----Dictionary values ------")
for val in e_data.values():  # list(e_data.values())
    print(val)


print("-----------3. items() ----------")
# 3. items() : To retrieve all items from dictionary
items = e_data.items()
print("E DATA Items : ", items, type(items))
items = list(items) # [('eid', 100), ('name', 'MadhuN') .... ]
print("E DATA Items : ", items, type(items))


n1, n2 = (1, 2)  # tuple unpacking
print("Values : ", n1, n2)

print("Iterating through dict items")
for item in e_data.items():
    print(item)

print("-------------------")

for key, val in e_data.items():
    print(key, " --- ", val)


# 4. update()
print("-----------4. update() ----------")
list1 = [1, 2, 3]
list2 = [4, 5, 6]  # [1,2,3,4,5,6]
list1.extend(list2)

dict1 = {1: 1, 2: 2}
dict2 = {3: 3, 4: 4}
dict1.update(dict2)
print("Dictionary Update  : ", dict1, dict2)

print("-----------5. clear() ----------")
di = {1: 1, 2: 2, 3: 3, 4: 4}
print("Before clear : ", di)
di.clear()
print("After clear : ", di)

print("-----------6. fromkeys() ----------")

di = {1: 1, 2: 2}
di = di.fromkeys([10, 20, 30, 40], "Hello")

print("Dictionary from keys : ", di)


print("-----------7. copy() ----------")
di1 = {1: 1, 2: 2}
di2 = di1.copy()
# di1 = di2
print("-----Before modification-----------")
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)
print("-----After modification-----------")
di2['name'] = 'Madhu'
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)

print("-----------8 . has_key() ----------")

dict1 = {1: 1, 2: 2, 'Hello': 'Madhu'}

'''
pop() popitem() setdefault()
'''

print("-----------8 . get() ----------")


# ecommerce:
my_order = {'orderno': 12123232,
           'ref_no': 324324,
           'items_qty': 4,
           'price': 324324,
           'del_addr': []
            }

# singup loginpage username password
e_data = {'eid': 43243,
          'name': 'MadhuN',
          'sal': 14000,
          'mobile': '7406900500',  # 91-7406900500
          'office': 'Bangalore'
          }
print("Employee data : ", e_data)
print("Employee name : ", e_data['name'])
print("Employee mobile  : ", e_data['mobile'])
# print("Employee name : ", e_data['company']) # error
print("Employee company : ", e_data.get('company'))  # to avoid exception
print("Employee sal     : ", e_data.get('sal', 1))
print("Employee company : ", e_data.get('company', 'ORACLE'))
# to set default value if key doesnot exists


print("Employee name : ", e_data.get('name'))
print("Employee name : ", e_data.get('mobile'))
print("Employee name : ", e_data.get('mobile', '----------'))
print("Employee name : ", e_data.get('company'))
print("Employee name : ", e_data.get('company', 'ORACLE'))

'''Aadhar card info '''

aadhar_deatils = {'a_no': 32423423213123,
                  'name': 'Madhu Nettem',
                  'email': 'nettemmadhu@gmail.com',
                  'mobile': '7406900500',
                  'location': 'Bangalore'
                  }


aadhar_deatils = {'a_no': 32423423213123,
                  'name': 'Madhu Nettem',
                  'location': 'Bangalore'
                  }

'''
Database:
-----------------------------------------------------------------------------
SNo A_NO       NAME         MOBILE       EMAIL                    LOCATION 
-----------------------------------------------------------------------------
11   3243243   madhu       7406900500    nettemmadhu@gmail.com    Bangalore
12   3243244   ramu        2433242344          xyz@gmail.com      Bangalore
------------------------------------------------------------------------------
'''