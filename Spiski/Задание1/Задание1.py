n = int(input()) 
a = [] 
 
for i in range(n): 
    ch = int(input())
    if abs(ch) <= 10**5:
        a.append(ch) 
a.reverse()
 
print(a)
