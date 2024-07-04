#백준 2606 바이러스 -

n = int(input())
m = int(input())
check = [0]*n

adj = [[] for j in range(n)]
ans =[]
c = []
for i in range(m):
  a,b = list(map(int,input().split()))
  adj[a-1].append(b-1)
  adj[b-1].append(a-1)

check[0] = 1

while True:
  new = False
  for i in range(n):
    if check[i] == 0:
      continue
    for j in adj[i]:
      if check[j] == 0:
        check[j] = 1
        new =True
  if not new:
    break
count = 0

for i in check:
  if i ==1:
    count +=1
print(count-1)