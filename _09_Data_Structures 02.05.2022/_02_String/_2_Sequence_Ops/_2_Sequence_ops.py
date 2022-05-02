# String sequence operations

message = 'HELLO WORLD'   # 0 1 2 3 4 5 6
print(message)

print("----String with for loop--------")
for char in message:
    print(char)

print("----String with for loop--------")
for char in message[0:5]:
    print(char)

print("----String with for loop--------")
for char in message[::-1]:
    print(char)

# SEQUENCE OPERATIONS
message = 'HELLO WORLD'
print("----------1. Indexing---------")
# 1. Indexing:
print("4th index : ", message[4])
print("7th index : ", message[7])
print("9th index : ", message[9])
print("9th index : ", message[-2])
print("10th index : ", message[10])
print("10th index : ", message[-1])


print("----------2. Slicing---------")
# 2. Slicing :
message = 'HELLO-WORLD'
print("2 to 5 : ", message[2:5])
print("3 to 7 : ", message[3:7])
print("-9 to 5 : ", message[-9:5])

print("----------3. Adding---------")
# 3. Adding :
str1 = 'Hello'
str2 = 'World'
print("Addition :", str1 + str2)
print("Addition :", str2 + str1)

str1 = 'Hello '
str2 = 'World'
print("Addition :", str1 + str2)
print("Addition :", str2 + str1)


print("----------3. Multiplying---------")
# 4. Multiplying
str1 = 'HELLO '
print(str1[3])
print("Multiplication :", str1 * 5)

print("----------4. Membership ---------")
# 5. Checking for membership
msg1 = 'HELLO-PYTHON'

print("H  : ", 'H' in msg1)
print("L  : ", 'L' in 'HELLO-PYTHON')
print("LL  : ", 'LL' in 'HELLO-PYTHON')
print("PH  : ", 'PH' in 'HELLO-PYTHON')
print("-  : ", '-' in 'HELLO-PYTHON')
print("Space  : ", ' ' in 'HELLO PYTHON')
print("B  : ", 'B' not in 'HELLO PYTHON')
message = 'HELLO-PYTHON'
print('H' in message)
print('L' in message)


str1 = 'HelloWorld'  # Refer ASCII table  A-Z 65-90    a-z 97....122

print("----------6. Length ---------")
# 6. len()
print("Length of string : ", len(str1))
#7. max()
print("----------7. Max ---------")
print("Max of string : ", max(str1))

#8. min()
print("----------8. Min ---------")
print("Min of string : ", min(str1))

'''
str1 = 'Hello World'


String str1 = new String("Hello World")
StringBuffer
StringBuilder
char = ''

emp_ids = [1,2,3,4,5,6,7] #list

List<Integer> list = new ArrayList<Integer>()
list.add(1)
list.add(2)
list.add(3)
list.add(4)
list.add(5)
'''