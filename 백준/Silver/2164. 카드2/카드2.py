from collections import deque
n = int(input())
l=deque([])
for i in range(1,n+1):
  l.append(i)

if n == 1:
  print(1)
else:
  while len(l)>1:
    l.popleft()
    l.append(l[0])
    l.popleft()

  print(l[0]) 
