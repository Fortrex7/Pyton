m = int(input())
n = int(input())
boat = 0
t = [int(input()) for i in range(n)]
if t[0] > m:
  print('Ves rybaka bolshe dopustimogo')
  exit()
while len(t):
  boat += 1
  k = m - t.pop(0)
  for j in range(len(t)):
    if t[j] <= k:
      t.pop(j)
      break
print(boat)