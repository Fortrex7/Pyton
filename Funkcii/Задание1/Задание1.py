def fac(n):

    if n == 0:

        return 1

    return fac(n-1) * n

y=int(input("Vvedite chislo: "))

print(f"Faktorial ot {y} = ", fac(y))

for i in range(fac(y),0,-1):

    print(f"Faktorial ot {i} = ", fac(i))