# Requirement:
# steps :
# state = data type
# behaviour = buisiness logical implementation
# validation = testing


x = float(input(" Enter the amount :"))
if x >= 10000:
    print(" your booking confirmed in the flight AR00012 with BUISINESS CLASS ")
elif x >= 5000:
    print(" your booking confirmed in the flight AR00012 with EXECUTIVE CLASS ")
elif x >= 2000:
    print(" your booking confirmed in the flight AR00012 with ECONOMY CLASS ")
else:
    print(" your booking not confirmed in the flight AR00012 ")