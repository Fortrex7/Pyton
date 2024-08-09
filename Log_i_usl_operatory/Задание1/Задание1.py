a = int(input())

if (a > 0) and (a % 2 == 0):
    print("Polozhitelnoe chetnoe chislo")
elif (a < 0) and (a % 2 == 0):
    print("Otricatelnoe chetnoe chislo")
elif (a == 0):
    print("Nulevoe chislo")
else:
    print("Chislo ne javjaetsja chetnym")