
n = int(input("Vvedite kolichestvo chisel: "))
print("Vvedite chisla: ")
cnt = 0
for i in range(n):
    ch = int(input())
    if ch == 0:
        cnt += 1
print("Kolichestvo chisel ravnyh 0: ", cnt)