'''
program showing all string methods
All string methods returns new values but do not change the original string
input : string
'''
import base64
import string
'''
# REQ: Get student exam result based on Marks 
----------------------------------------------
STATE    : Marks
BEHAVIOR : Get student exam result


'''
# REQ: Get string with capital letter
# STATE
str1 = 'hello world'  # 'HELLO WORLD'  'Hello World'
# BEHAVIOR
print("String with capital : ", str1.capitalize())

100
print(10)
x = 20
print(x)
print(x*x)
# String Functions/Methods  40

# 1. capitalize() :: Returns a string where the first character is upper case.

print("------------- 1. capitalize() -----------------")
print("capitalize() : capitalizes first letter of given input string")

str1 = 'hello world' # HELLO  ===> Hello
print("Normal string            :", str1)
str1.capitalize()  # Hello world   10
print("String after capitalize  :", str1)
print("String after capitalize! :", str1.capitalize())   # print(10)
print("String after capitalize!!:", str1)
str2 = str1.capitalize()                     # x = 10
print("String after capitalize  :", str2)    # print(x)

'''3 Ways'''
print("----Way 1--------")
# 1 : Current string should be used as is, new string used "one time"
str1 = 'hello world'
print("String     : ", str1)
print("Capitalize : ", str1.capitalize())  # print(10)
print("String     : ", str1)

# 2 : Current string should be used as is, new string used in "multiple places"
print("----Way 2--------")
str1 = 'hello world'
print("String     : ", str1)
str2 = str1.capitalize()         # x = 10
print("String     : ", str1)
print("String     : ", str2)     # print(x)

# 3 : Current string should get modified
print("----Way 3--------")
str1 = 'hello world'
print("String     : ", str1)
str1 = str1.capitalize()
print("String     : ", str1)

print("-------------------------------------------------------------------------------------")


# 2. center() : Returns a space-padded string with the original string centered to a total of width columns.
print("------------- 2. center() -----------------")

print("center() : returns center padded string with mentioned length")

str1 = 'hello world'
print("Normal string                                                :", str1)

print("String after center function with width 28 & fillchar as $   :", str1.center(28, '#'))
print("String after center function with width 24                   :", str1.center(24))
print("-------------------------------------------------------------------------------------")


# 3. count() : Counts how many times str occurs in string or in a substring of string.
str1 = 'hello world'
print("------------- 3. count() -----------------")
print('count() : Counts how many times str occurs in string or in a substring of string.')

print("Normal string                           :", str1)

print("Number of e's in the total string are   :", str1.count('e', 0, len(str1)))
print("Number of l's in the total string are   :", str1.count('l', 0, len(str1)))
print("-------------------------------------------------------------------------------------")


# 4. decode() : Decodes the string using the codec registered for encoding.
str1 = 'hello world'
str2 = str1.encode('UTF-8')  # encode convert into bytes
print("------------- 4. decode() -----------------")
print('decode() : Decodes the string using the codec registered for encoding..')

print("Encoded string        :", str2)
print("Decoded string        :", str2.decode('UTF-8', 'string'))
print("-------------------------------------------------------------------------------------")


# 5. encode() : Returns the encoded version of the string.
str1 = 'hello world'
print("------------- 5. encode() -----------------")
print('encode() : Returns the encoded version of the string.')

print("Normal  string        :", str1)
print("Encoded string        :", str1.encode('UTF-8', 'strict'))
print("-------------------------------------------------------------------------------------")


# 6. endswith() : returns true if end with mentioned suffix.
str1 = 'hello world'
print("------------- 6. endswith() -----------------")
print('endswith() : returns true if end with mentioned suffix.')

print("Normal string                           :", str1)

print("If the Normal String ends with pe or not:", str1.endswith("pe", 5, 12))
print("If the Normal String ends with ld or not:", str1.endswith("ld", 2, 8))
print("If the Normal String ends with ld or not:", str1.endswith("ld", 3, 12))
print("-------------------------------------------------------------------------------------")


# 7. expandtabs() : expands tab to mentioned spaces, 8 being default.
str1 = 'hello world'
print("------------- 7. expandtabs() -----------------")
print('expandtabs() : expands tab to mentioned spaces, 8 being default.')

print('without expandtabs() :', str2)
print('expandtabs()         :', str1.expandtabs(22))
print("-------------------------------------------------------------------------------------")

#8. find() : returns the index position found within mentioned limits or it  returns -1 if not found.
str1 = "chesapeake ripper"
str2 = "Hannibal\tLecter"
print("------------- 8. find() -----------------")
print('find() : returns the index (within mentioned limits) \n returns -1 if not found')

print("index of ash,if present in chesapeake ripper between index 0 & 21     :", str1.find("ash", 0, 21))
print("index of  rip,if present in chesapeake ripper                         :", str1.find(" rip"))
print("index of lec,if present in Hannibal\tLecter between index 3 & 14      :", str2.find("ec", 3, 14))
print("index of peak,if present in chesapeake ripper between index 8 & 12    :", str1.find("peak", 0, 12))
print("-------------------------------------------------------------------------------------")

# 9. index() : returns the index (within mentioned limits) \n else raises exception'
str1 = "chesapeake ripper"
str2 = "Hannibal\tLecter"

print("------------- 9. index() -----------------")
print('index() : returns the index (within mentioned limits) \n else raises exception')
print("index of pea in chesapeake ripper,if present between index 3 & 18", str1.index("pea", 3, 18))
print("-------------------------------------------------------------------------------------")

print('********** is methods return true or false **********')

print("-------------------------------------------------------------------------------------")

# 10. isalnum() : returns true if string is alphanumeric
str1 = "chesapeake ripper"
str2 = "Hannibal\tLecter"
str3 = "Aug231994"
print("------------- 10. isalnum() -----------------")
print('isalnum() : returns true if string is alphanumeric')
print("chesapeake ripper is alphanumeric    :", str1.isalnum())
print("Aug231994 is alphanumeric            :", str3.isalnum())
print("-------------------------------------------------------------------------------------")


# 11. isalpha() : returns true if all substrings are alphabets.
str1 = "chesapeake"
substr1 = "ake"

print("------------- 11. isalpha() -----------------")
print('isalpha() : returns true if all substrings are alphabets')
print("chesapeake ripper contains only alphabets    :", str1.isalpha())
print("ake contains only alphabets                  :", substr1.isalpha())
print("-------------------------------------------------------------------------------------")


# 12. isdigit() :  returns True if all characters in the string are digits.
num_str1 = "23081994"
substr1 = "ake"

print("------------- 12. isdigit() -----------------")
print('isdigit() : returns True if all characters in the string are digits')
print("ake contains all digits      :", substr1.isdigit())
print("23081994 contains all digits :", num_str1.isdigit())
print("-------------------------------------------------------------------------------------")



# 13. islower() : returns True if all characters are in lowercase
str1 = "chesapeake ripper"
str2 = "Hannibal\tLecter"

print("------------- 13. islower() -----------------")
print('islower() : returns True if all characters are in lowercase')
print("chesapeake ripper is all lower    :", str1.islower())
print("Hannibal\tLecter is all lower     :", str2.islower())
print("-------------------------------------------------------------------------------------")



# 14. isnumeric() : returns true if all characters in the string are numeric
num_str1 = "23081994"
num_str2 = u"16041991"
str3 = "Aug231994"
print("------------- 14. isnumeric() -----------------")
print('isnumeric() : returns true if all characters in the string are numeric')
print("Aug231994 is numeric   :", str3.isnumeric())
print("23081994 is numeric    :", num_str1.isnumeric())
print("u16041991 is numeric   :", num_str2.isnumeric())
print("-------------------------------------------------------------------------------------")


# 15. isspace() : returns true if all characters in the string are whitespaces
str1 = "chesapeake ripper"
str2 = "Hannibal\tLecter"
empty_str1 = "  "
print("------------- 15. isspace() -----------------")
print('isspace() : returns true if all characters in the string are whitespaces')
print("chesapeake ripper is space   :",str1.isspace())
print("   is space                  :", empty_str1.isspace())
print("-------------------------------------------------------------------------------------")

# 16. istitle() : returns true if string is in titlecase
str1 = "chesapeake ripper"
str2 = "Hannibal\tLecter"
print("------------- 16. istitle() -----------------")
print('istitle() : returns true if string is in titlecase')
print("Hannibal\tLecter is title    :", str2.istitle())
print("chesapeake ripper is title   :", str1.istitle())
print("-------------------------------------------------------------------------------------")


# 17. isupper() : returns True if all characters are in uppercase
str1 = "chesapeake ripper"
str4 = "HELLO"
print("------------- 17. isupper() -----------------")
print('isupper() : returns True if all characters are in uppercase')
print("chesapeake ripper is upper   :", str1.isupper())
print("HELLO is upper               :", str4.isupper())
print("-------------------------------------------------------------------------------------")


# 18. join() : joins strings with mentioned separator
sep_str = "****"
seq1 = ["The", "sky", "is", "Blue"]
print("------------- 18. join() -----------------")
print('join() : joins strings with mentioned separator')
print("join [The, sky, is, Blue] with ****: ", sep_str.join(seq1))
print("-------------------------------------------------------------------------------------")



# 19. len() : returns length
sep_str = "****"
str2 = "Hannibal\tLecter"
seq1 = ["The", "sky", "is", "Blue"]
print("------------- 19. len() -----------------")
print("len() : returns length")
print("Length of Hannibal\tLecter           :", len(str2))
print("Length of The****sky****is****Blue   :", len(sep_str.join(seq1)))
print("-------------------------------------------------------------------------------------")


# 20. ljust() : adjust length to mentioned number with provided char on right
substr1 = "ake"
print("------------- 20. ljust() -----------------")
print('ljust() : adjust length to mentioned number with provided char on right')
print("The string is            :", substr1)
print("ljust(10,*) of ake is    :", substr1.ljust(10, "*"))
print("-------------------------------------------------------------------------------------")



# 21. lower() : converts string to all lowercase characters
str2 = "Hannibal\tLecter"
print("------------- 21. lower() -----------------")
print('lower() : converts string to all lowercase characters')
print("Asha in lower characters is  :", "Asha".lower())
print("Hannibal\tLecter in lower is :", str2.lower())
print("-------------------------------------------------------------------------------------")


# 22. lstrip() : removes mentioned char (left)
str5 = "    The dress looks fab  "
str6 = "***Wow! what a great move**"
print("------------- 22. lstrip() -----------------")
print('lstrip() : removes mentioned char (left)')
print("lstrip of " " in The dress looks fab           :", str5.lstrip(" "))
print("lstrip of * in  ***Wow! what a great move**    :", str6.lstrip("*"))
print("-------------------------------------------------------------------------------------")


# 23. maketrans() : Returns a translation table to be used in translate function.
trans_string = "Dr. Hannibal Lecter is a fictional character in a series of suspense novels by Thomas Harris."
# trans_table = maketrans("aioshc","@!0$#(")
print("------------- 23. maketrans() -----------------")
print('maketrans() : Returns a translation table to be used in translate function.')
print("translation table:", str.maketrans("aioshc", "@!0$#("))
print("-------------------------------------------------------------------------------------")


# 24. max(str) : Returns the max alphabetical character from the string str.(Using ASCII Values)
str5 = "The dress looks fab"
str6 = "***Wow! what a great move***"
print("------------- 24. max(str) -----------------")
print('max(str) : Returns the max alphabetical character from the string str.(Using ASCII Values)')
print("max of (The dress looks fab is)         :", max(str5))
print("max of (***Wow! what a great move**)    :", max(str6))
print("-------------------------------------------------------------------------------------")

# 25. min(str) : Returns the min alphabetical character from the string str.(Using ASCII Values)
str5 = "The dress looks fab"
str6 = "***Wow!*"
print('------------- 25. min(str) -----------------')
print('min(str) : Returns the max alphabetical character from the string str.(Using ASCII Values)')
print("min of (The dress looks fab is)  :", min(str5))
print("min of (***Wow!*)                :", min(str6))
print("-------------------------------------------------------------------------------------")


# 26. replace(old, new [max]) : replace with given char
str1 = "chesapeake ripper"
print('------------- 26. replace() -----------------')
print('replace() : replace with given char')
print("Replace a with @ in chesapeake ripper only once          :", str1.replace("a", "@", 1))
print("Replace all a's with @ in chesapeake ripper              :", str1.replace("a", "@"))
print("Replace all a's with @ and i with ! in chesapeake ripper :", (str1.replace("a", "@")).replace("i", "!"))
print("-------------------------------------------------------------------------------------")

# 27. rfind() : returns the index (within mentioned limits) \n returns -1 if not found.
str1 = "chesapeake ripper"
print("------------- 27. rfind() -----------------")
print('rfind() : searches from last and gives index')
print("index of e from the last of chesapeake ripper is                            :", str1.rfind("e"))
print("index of e from the right in between index 1 and 12 of chesapeake ripper is :", str1.rfind("e", 1, 12))
print("-------------------------------------------------------------------------------------")


# 28. rindex() : Same as index(), but search backwards in string'
str1 = "chesapeake ripper"
str2 = "Hannibal\tLecter"

print("------------- 28. rindex() -----------------")
print('rindex() : returns the index (within mentioned limits) \n else raises exception')
print("index of pea in chesapeake ripper,if present between index 3 & 18 from right     :", str1.index("pea", 3, 18))
print("index of eak in chesapeake ripper,if present between index 2 and 18 from right   :", str1.rindex("eak", 2, 18))
print("-------------------------------------------------------------------------------------")


# 29. rjust() : adjust length to mentioned number with provided char on left
substr1 = "ake"
print("------------- 29. rjust() -----------------")
print('rjust() : adjust length to mentioned number with provided char on left')
print("The string is            :", substr1)
print("rjust(10,*) of ake is    :", substr1.rjust(10, "*"))
print("-------------------------------------------------------------------------------------")


# 30. rstrip() : removes mentioned char (right)
str5 = "    The dress looks fab  "
str6 = "***Wow! what a great move**"
print("------------- 30. rstrip() -----------------")
print('rstrip() : removes mentioned char (right)')
print("rstrip of " " in The dress looks fab          :", str5.rstrip(" "))
print("rstrip of * in ***Wow! what a great move**    :", str6.rstrip("*"))
print("-------------------------------------------------------------------------------------")


# 31. split() : separates with spaces into lists
str1 = "hello world"
str5 = "    The dress looks fab  "
print("------------- 31. split() -----------------")
print('split() : separates with spaces into lists ')
print("Original String:", str1)
print("Splitting chesapeake ripper:", str1.split())
print("-----------------------------------------------")
print("Original String                    :", str5)
print("Splitting     The dress looks fab  :", str5.split(" ", 3))
print("-------------------------------------------------------------------------------------")



# 32. splitlines() : splits at line breaks & returns lists
str6 = "***Wow! what a great move**"
str7 = "Scary \n dream\n haunts him every \n night"
print("------------- 32. splitlines() -----------------")
print('splitlines() : splits at line breaks & returns lists ')
print("Original String:", str6)
print("Splitting lines for the original string is:", str6.splitlines())
print("-----------------------------------------------")
print("Original String                             :", str7)
print("Splitting lines for the original string is  :", str7.splitlines(True))
print("Splitting lines for the original string is  :", str7.splitlines(2))
print("-------------------------------------------------------------------------------------")

# 33. startswith() : returns true if list starts with given char
str1 = "chesapeake ripper"
print("------------- 33. startswith() -----------------")
print('startswith() : returns true if list starts with given char')
print("Original String                                              :", str1)
print("chesapeake ripper starts with pe in between index 1 and 12   :", str6.splitlines())
print("---------------------------------------------------------------------")
print("Original String                                              :", str1)
print("chesapeake ripper starts with pe in between index 5 and 12   :", str1.startswith("pe", 5, 12))
print("----------------------------------------------------------------------")
print("Original String                                              :", str1)
print("chesapeake ripper starts with pe                             :", str1.startswith("pe"))
print("----------------------------------------------------------------------")
print("Original String                                              :", str1)
print("chesapeake ripper starts with pe                             :", str1.startswith("ch"))
print("-------------------------------------------------------------------------------------")


# 34. strip() : Performs both lstrip() and rstrip() on string.
str5 = "    The dress looks fab  "
str6 = "***Wow! what a ** great move**"
print("------------- 34. strip() -----------------")
print('strip() : Performs both lstrip() and rstrip() on string')
print("strip of " " in The dress looks fab          :", str5.strip(" "))
print("strip of * in ***Wow! what a ** great move**    :", str6.strip("*"))
print("-------------------------------------------------------------------------------------")


# 35. swapcase() : Inverts case for all letters in string.
str2 = "Hannibal\tLecter"
print("------------- 35. swapcase() -----------------")
print('swapcase() : swaps case')
print("Original String is                            :", str2)
print("Swaping the case of Hannibal\tLecter        :", str2.swapcase())
print("-------------------------------------------------------------------------------------")


# 36. title() : returns titlecase (Capitalize each word of the string).
str5 = "    The dress looks fab  "
str6 = "***Wow! what a ** great move**"
print("------------- 36. title() -----------------")
print('title() : returns titlecase')
print("Original String is                          :", str5)
print("Title of string The dress looks fab         :", str5.title())
print("-----------------------------------------------")
print("Original String is                          :", str6)
print("Title of ***Wow! what a ** great move**     :", str6.title())
print("-------------------------------------------------------------------------------------")

# 37. translate() : Translates string according to translation table str(256 chars), removing those in the del string..
print("------------- 37. translate() -----------------")
print('translate(): Translates string according to translation table str(256 chars), removing those in the del string.')
trans_string = "Dr. Hannibal Lecter is a fictional character in a series of suspense novels by Thomas Harris."
# trans_table = maketrans("aioshc","@!0$#(")
print("Original String is:")
print(trans_string)
print("\n")
print("Translated String is:")
print(trans_string.translate(str.maketrans("aioshc", "@!0$#(")))
print("-------------------------------------------------------------------------------------")


# 38. upper() : Converts lowercase letters in string to uppercase.
print("------------- 38. upper() -----------------")
print("upper() : Converts lowercase letters in string to uppercase.")
str1 = 'hello world'
print("Normal string               :", str1)
print("String in upper case is     :", str1.upper())
print("-------------------------------------------------------------------------------------")


# 39. zfill(width) : Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).
print("------------- 39. zfill() -----------------")
print('zfill() : adds 0 at start to make up the length')
str1 = 'hello world'
print("zfill of hello world is      :", str1.zfill(len(str1) + 2))
print("zfill(20) of hello world is  :", str2.zfill(20))
print("-------------------------------------------------------------------------------------")


# 40. isdecimal() : returns true if all characters in the string are numeric
num_str1 = "23081994"
num_str2 = u"16041991"
str3 = "Aug231994"
num_str4 = "-259.6"
print("------------- 40. isdecimal() -----------------")
print('isdecimal() : returns true if all characters in the string are numeric')
print("23081994 is decimal   :", num_str1.isdecimal())
print("u16041991 is decimal  :", num_str2.isdecimal())
print("Aug231994 is decimal  :", str3.isdecimal())
print("-259.6 is decimal     :", num_str4.isdecimal())
print("-------------------------------------------------------------------------------------")

'''


# Difference between isdecimal /isdigit /isnumeric:
"""
+-------------+-----------+-------------+----------------------------------+
| isdecimal() | isdigit() | isnumeric() |          Example                 |
+-------------+-----------+-------------+----------------------------------+
|    True     |    True   |    True     | "038", "੦੩੮", "０３８"           |
|  False      |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧"          |
|  False      |  False    |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參"  |
|  False      |  False    |  False      | "abc", "38.0", "-38"             |
+-------------+-----------+-------------+----------------------------------+
'''


str = 'mani'
str1=(str.title())
print(str1.find('M', 0, 4))
