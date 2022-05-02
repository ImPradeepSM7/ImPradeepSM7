print("-------For loop with dictionary--------")

emp_details = {'eid': 100,
               'ename': 'MadhuN',
               'sal': 12500}

print("------All Items-------")
for key, val in emp_details.items():
    print(key, val)

print("------All Keys-------")
for key in emp_details.keys():
    print(key)

print("------All Values-------")
for val in emp_details.values():
    print(val)

print("--------Only keys------")
for val in emp_details:
    print(val)