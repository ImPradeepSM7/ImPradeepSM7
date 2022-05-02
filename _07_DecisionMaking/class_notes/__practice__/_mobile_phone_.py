# mobile phone purchase in a shop

x = int(input("Enter your purchase amount limit :"))
if (x <= 50000) and (x >= 40000):
    print("select iPHONE models")
elif (x <= 40000) and (x >= 30000):
    print(" select ONE PLUS models")
elif (x <= 30000) and (x >= 20000):
    print("select SAMSUNG models")
elif (x <= 20000) and (x >= 10000):
    print("Select HONOR, OPPO, MI models")
else:
    print(" HAVE A NICE DAY , not available in your range")

