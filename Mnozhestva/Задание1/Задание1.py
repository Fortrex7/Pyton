n=int(input())
spisok = list(map(int, input().split()))[:n]
e=set(spisok)
print(len(e))