# 2. center() : Returns a space-padded string with the original string centered to a total of width columns.
print("------------- 2. center() -----------------")

print("center() : returns center padded string with mentioned length")


str1 = 'hello world'
str2 = 'hello world welcome'
print("Normal string                                                :", str1)
print("Length after padding : ",len(str1.center(28, '$')))
print("String after center function with width 28 & fillchar as $   :", str1.center(28, '^'))
print("String after center function with width 28 & fillchar as $   :", str2.center(28, '^'))
print("String after center function with width 24                   :", str1.center(24))
print("-------------------------------------------------------------------------------------")

from collections import defaultdict

# Defining the dict and passing
# lambda as default_factory argument
d = defaultdict(str)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
print(d['id'])