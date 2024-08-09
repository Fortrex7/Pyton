a = int(input("Vvedite chislo A: "))
b = int(input("Vvedite chislo B: "))
cnt = []
if a <= b:
    for i in range(a, b + 1):
        if i % 2 == 0:
            cnt.append(i)
    print("Chetnye chisla iz diapazona ot A do B: ", cnt)
else:
    print("A dolzno byt' men'she B")