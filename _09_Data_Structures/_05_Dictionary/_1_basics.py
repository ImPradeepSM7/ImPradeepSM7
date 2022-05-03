dict1 = {"key":"value", 1:"mani", 2:"mani", }

'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable 
and do not allow duplicates keys.

used to store data values like a map, 
which, unlike other Data Types that hold only a single value as an element,

Dictionary holds key:value pair. Key-value is provided in the dictionary to make
it more optimized.


'''




list1 = [1, 2, 3, 4, 5]
m_bill = [11.2, 124, 32, 213, 43]
e_data = [100, 'Madhu Nettem', 45000, 'Male', 'Bangalore', '560037', ['123', 'Marthahalli']]
# address
print("Employee data : ", e_data)

order_details = [12123321, 2133213, 12323, 'TLEE234e3', 43243, '43242']

# Immutable: int float bool string tuple
# Mutable  : list, dict, set
e_data = {'eid': 100,
          'name': 'Madhu Nettem',
          'sal': 45000,
          'gender': 'Male',
          'loc': 'Bangalore',
          'pin': '560037',
          'address': {'hno': '123', 'area': 'marthahalli'},
          'sal':444
          }
print("=====================",e_data)
e_data["emp_id"] = "1089675"
print(e_data)
print("=================================")
print(e_data)
#mobile_no = 900990090000  # static way
mobile_no = int(input("Enter mobile no :"))  # dynamic input
e_data['mobile_no'] = mobile_no
# create list.iterate through


print("Dictionary : ", e_data)
print("Emp sal    :", e_data['sal'])
print("Emp area   : ", e_data['address']['area'])

print("----------Extracting dictionary----------")
print(e_data)
print(e_data.items())
print(e_data.values())
print(e_data.keys)


for key, val in e_data.items():
    print(key,"-----", val)






# UI ---> Python ----> Database
'''
Signup 
-----------
firstname : Madhu
lastname  : Nettem
mobileno  : 7406332332
mailid    : xyz@gmail.com
userid    : xyz
password  : xyz@13
gender    : Male
location  : Bangalore   # json format 


'''

order_details = [123213, 3432, 'Madhu Nettem', 'Bangalore', 543.56, 23, 5, '560037', 4]

order_details = {'order_no': 123213,
                 'ref_no': 3432,
                 'cust_name': 'Madhu Nettem',
                 'del_loc': 'Bangalore',
                 'total_bill': 543.56,
                 'discount': 23,
                 'disc_percnt': 5,
                 'pin_code': 560037,
                 'no_of_items': 4,
                 }


print("Order details : ", order_details)
print("Location : ", order_details['del_loc'])
print("Order No : ", order_details['order_no'])
# print("Order No : ", order_details[100])


'''
Dictionary : 
    - Mutable data structure
    - Unordered
    - Key value pair i.e, item 
    Key properties:
        - Keys must be UNIQUE
        - Keys must be IMMUTABLE and values can be anything
        
'''
# 1. Keys must be IMMUTABLE and values can be anything
dict1 = {100: 10,
         200: {1: 1, 2: 2},
         102.3: 29,
         True: 'Madhu',
         'Message': [1, 2, 3, 4, 5],
         (1, 2, 3): (1, 2, 3),
         # [1,2,3] : {1:1,2:2},  # Wrong, List is mutable
         # {1:1,2:2} : "Hello"   # Wrong, dict is mutable
         # {1,2,3} : "Hello"     # Wrong, set is mutable
         }

print("Keys immutable : ", dict1)
# Dict keys should not be List, Dictionary, Set

# 2. Keys must be unique
x = 10
x = 20

dict1 = {10: 100,
         20: 100,

         }
print("Keys must be unique :", dict1)
