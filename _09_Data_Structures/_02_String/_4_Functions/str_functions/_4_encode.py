# 4. decode() : Decodes the string using the codec registered for encoding.
str1 = 'hello world'
str2 = str1.encode('UTF-8', 'strict')
print("------------- 4. decode() -----------------")
print('decode() : Decodes the string using the codec registered for encoding..')

print("Encoded string        :", str2)
print("Decoded string        :", str2.decode('UTF-8', 'strict'))

str1 = 'hello'
str2 = str1.encode()
print("Normal  : ",str1 )
print("Encoded : ", str2)
print("Decoded : ", str2.decode())