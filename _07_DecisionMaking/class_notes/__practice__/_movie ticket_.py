# Requirement
# sofa = 250
# Balcony = 200
# lounge = 100

y = int(input("Enter the amount you have :"))

if y >= 250:
    print("Get your Premium Lounge ticket")
elif y >= 200:
    print(" Get your Balcony ticket")
elif y >= 150:
    print("Get your Lounge ticket")
else:
    print("No ticket ")
