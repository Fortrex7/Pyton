n = int(input())
lst = list(map(int, input().split()))[:n]

lst.insert(0, lst.pop())
print(lst)