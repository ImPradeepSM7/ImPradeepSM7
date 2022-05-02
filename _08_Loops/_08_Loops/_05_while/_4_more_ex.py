
# Arithmetic, Comparasion, Logical
print("--------Numbers div 5 or 8, not by 3 -----------")
# Numbers between 1 to 100 divisible by either 5 or 8, should not divisible 3

n1 = 1
n2 = 50
while n1 <= n2: #true
    if n1 % 5 == 0 or n1 % 8 == 0: # 15 True
        if n1 % 3 != 0:  # 15 / 3  False
            print(n1)

    n1 += 1
