'''
program showing all string methods
All string methods returns new values but do not change the original string
input : string
'''
import base64
import string

# str1 = str(input('Enter string'))
# Different string initlization examples
str1 = "chesapeake ripper"
substr1 = "ake"
str2 = "Hannibal\tLecter"
str3 = "Aug231994"
str5 = "    The dress looks fab  "
str6 = "***Wow! what a great move**"
str7 = "Scary \n dream\n haunts him every\nnight"
num_str1 = "23081994"
num_str2 = u"16041991"
empty_str1 = "  "
sep_str = "****"

# String Methods

# 1. capitalize() :: Returns a string where the first character is upper case.

print("------------- 1. capitalize() -----------------")

print("capitalize() : capitalizes first letter of given input string")

str1 = 'hello world'
print("Normal string           :", str1)
str1.capitalize()
print("String after capitalize :", str1.capitalize())
print("-----------------------------------------------")


# 2. upper() :: Returns a string where the first character is upper case.

print("------------- 2.UPPER () -----------------")
print("UPPER() :convert all elements into uppercase of given input string")

str1 = 'hello world'
print("Normal string           :", str1)
str1.upper()
print("String after upper :", str1.upper())
print("-----------------------------------------------")


# str1 = str1.encode('base64', 'strict')
print('center() : returns center padded string with mentioned length')
print(str1.center(28, '$'))
print(str1.center(24))
print("-------------------------------------------------------------------")
print('count() : returns count of mentioned character')
print(str1.count('e', 0, len(str1)))
print(str1.count('x', 0, len(str1)))
# print(str1.decode('base64', 'strict'))
# print(str1.encode('base64', 'strict'))
print("-------------------------------------------------------------------")
print('endswith() : returns true if end with mentioned suffix')
print(str1.endswith("pe", 5, 12))
print(str1.endswith(substr1, 2, 10))
print("-------------------------------------------------------------------")
print('expandtabs() : expands tab to mentioned spaces, 8 being default')
print('without expandtabs():', str2)
print('expandtabs(): ', str2.expandtabs(7))
print("-------------------------------------------------------------------")
print('find() : returns the index (within mentioned limits) \n returns -1 if not found')
print(str1.find("ash", 0, 21))
print(str1.find(" rip"))
print(str2.find("lec", 3, 14))
print(str1.find("peak", 8, 12))
print("-------------------------------------------------------------------")
print('index() : returns the index (within mentioned limits) \n else raises exception')
#print(str1.index("pea", 3, 18))
#print(str1.rindex("eak", 2, 18))
print("-------------------------------------------------------------------")
print("-------------------------------------------------------------------")
print('is methods return true or false')
print('isalnum() : returns true is string alphanumeric')
print(str1.isalnum())
print(str3.isalnum())
print("-------------------------------------------------------------------")
print('isalpha() : returns true if all substrings are alphabets')
print(str1.isalpha())
print(substr1.isalpha())
print("-------------------------------------------------------------------")
print('isdigit() : returns True if all characters in the string are digits')
print(substr1.isdigit())
print(num_str1.isdigit())
print("-------------------------------------------------------------------")
print('islower() : returns True if all characters are in lowercase')
print(str1.islower())
print(str2.islower())
print("-------------------------------------------------------------------")
print('isupper() : returns True if all characters are in uppercase')
print(str1.isupper())
#print(str4.isupper())
print("-------------------------------------------------------------------")
print('isnumeric() : returns true if all characters in the string are numeric')
print(str3.isnumeric())
print(num_str1.isnumeric())
print(num_str2.isnumeric())
print("-------------------------------------------------------------------")
print('isspace() : returns true if all characters in the string are whitespaces')
print(str1.isspace())
print(empty_str1.isspace())
print("-------------------------------------------------------------------")
print('istitle() : returns true if string is in titlecase')
print(str2.istitle())
print(str1.istitle())
print("-------------------------------------------------------------------")
print('lower() : converts string to all lowercase characters')
print("Asha".lower())
print(str2.lower())
print("-------------------------------------------------------------------")
print('join() : joins strings with mentioned separator')
seq1 = ["The", "sky", "is", "Blue"]
print(sep_str.join(seq1))
print("-------------------------------------------------------------------")
print('len() : returns length')
print(len(str2))
print(len(sep_str.join(seq1)))
print("-------------------------------------------------------------------")
print('ljust() : adjust length to mentioned number with provided char on right')
print(substr1.ljust(10, "*"))
print("-------------------------------------------------------------------")
print('strip() : removes mentioned char (left , right)')
print(str6.strip("*"))
print(str5.strip())
print(str5.lstrip(" "))
print(str5.rstrip(" "))
print(str6.lstrip("*"))
print(str6.rstrip("*"))
print("-------------------------------------------------------------------")
print('replace() : replace with given char')
print(str1.replace("a", "@", 1))
print(str1.replace("a", "@"))
print((str1.replace("a", "@")).replace("i", "!"))
print("-------------------------------------------------------------------")
print('rfind() : searches from last and gives index')
print(str1.rfind("e"))
print(str1.rfind("e", 1, 12))
print(str1.rjust(25))
print(str1.rjust(25, "-"))
print("-------------------------------------------------------------------")
print('split() : separates with spaces into lists ')
print(str1.split())
print(str5.split(" ", 3))
print("-------------------------------------------------------------------")
print('splitlines() : splits at line breaks & returns lists ')
print(str6.splitlines())
print(str7.splitlines())
print(str7.splitlines(True))
print(str7.splitlines(2))
print("-------------------------------------------------------------------")
print('startswith() : returns true if list starts with given char')
print(str1.startswith("pe", 1, 12))
print(str1.startswith("pe", 5, 12))
print(str1.startswith("pe"))
print(str1.startswith("ch"))
print("-------------------------------------------------------------------")
print('swapcase() : swaps case')
print(str2.swapcase())
print("-------------------------------------------------------------------")
print('title() : returns titlecase')
print(str6.title())
print(str5.title())
print("-------------------------------------------------------------------")
print('zfill() : adds 0 at start to make up the length')
print(str1.zfill(len(str1) + 2))
print(str2.zfill(20))
print("-------------------------------------------------------------------")
print('maketrans() & translate()')
trans_string = "Dr. Hannibal Lecter is a fictional character in a series of suspense novels by Thomas Harris."
# trans_table = maketrans("aioshc","@!0$#(")
print(trans_string.translate(str.maketrans("aioshc", "@!0$#(")))