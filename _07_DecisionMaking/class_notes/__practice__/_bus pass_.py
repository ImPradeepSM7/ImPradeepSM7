# Bus pass

# Requirement: deluxe pass = 1190
# metro pass = 1090
# ordinary pass = 990
# student pass = 650

x = int(input("Enter the amount :"))
if x < 649 or x >= 1191:
    print("Enter valid amount :")
if x >= 1190:
    print("Deluxe pass")
elif x >= 1090:
    print("Metro express pass")
elif x >= 990:
    print("ordinary pass")
elif x >= 650:
    print("student pass")
else:
    print("no pass")
