chisla = {}

for k in range(10, -6,-1):
    chisla[k] = k ** k
for key, value in chisla.items():
    print(f"{key}: {value}")
