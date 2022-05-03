t1 = (1, 2, 3, 4, 5)

#t1 = t1.append(10)  # ERROR Tuple is immutable
print(t1)
t1 = (1, 2, 3, [4, 5, 6], 7)
# t1[3] = 100 # ERROR
print("Before -- ", t1)

t1[3].append(100)

print("After -- ", t1)

t2 = list(t1)
print(t2)