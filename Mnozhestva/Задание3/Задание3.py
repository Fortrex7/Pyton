a = list(map(int, input().split()))
s = set()
for i in a:
    print('YES ' if i in s else 'NO ', end = '')
    s.add(i)