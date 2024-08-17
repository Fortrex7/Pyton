import random

m = int(input("Введите колличество элементов по горизонтали: "))
n = int(input("Введите колличество элементов по вертикали: "))
a1 = int(input("Диапазон чисел в матрице 1:\nот "))
b1 = int(input("до "))
a2 = int(input("Диапазон чисел в матрице 2:\nот "))
b2 = int(input("до "))

matrix_1 = [[random.randint(a1,b1) for i in range(m)] for i in range(n)] # матрица 1 # диапазон randint() вводится с клавиатуры
matrix_2 = [[random.randint(a2,b2) for i in range(m)] for i in range(n)] # матрица 2 # диапазон randint() вводится с клавиатуры
matrix_3 = [[0 for i in range(m)] for i in range(n)] # сумма матриц 1 и 2

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        matrix_3[i][j] = matrix_1[i][j]+matrix_2[i][j]

def pr(n):
    for i in n:
        print(i)
        
print("matrix_1:")    
pr(matrix_1)
print("matrix_2:")    
pr(matrix_2)
print("Сумма matrix_1 и matrix_2:")   
pr(matrix_3)