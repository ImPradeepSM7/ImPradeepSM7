
# 3. count() : Counts how many times str occurs in string or in a substring of string.
str1 = 'hello world'
print("------------- 3. count() -----------------")
print('count() : Counts how many times str occurs in string or in a substring of string.')

str1 = 'helloworldhell'
print("Slicing :", str1[0:10])
print("Normal string : o  ", str1.count('o'))
print("Normal string : l  ", str1.count('l'))
print("Normal string : he ", str1.count('he'))
print("Normal string : world ", str1.count('world'))
print("Normal string : name  ", str1.count('name'))
print("Normal string : l  ", str1.count('l', 0, 10))

print("Normal string                           :", str1)

print("Number of e's in the total string are   :", str1.count('e', 0, 14))
print("Number of x's in the total string are   :", str1.count('x', 0, 13))
print("-------------------------------------------------------------------------------------")
