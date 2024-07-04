n = int(input())
m = int(input())

adj = [[] for j in range(n)]
check = [0] * n

for i in range(m):
  a,b = list(map(int, input().split()))
  adj[a-1].append(b-1)
  adj[b-1].append(a-1)

check[0] = 1
ans=[]
ans2=[]
# for kk in adj[0]:
#   ans.append(adj[kk])

# for ss in ans:
#   ans2 = ss+ans2

# ans3 = list(set(ans2))

while True:
  new = False
  for i in range(n):
    if check[i] == 0:
      continue
    for j in adj[i]:
      if i in (adj[0]+[0]):
        if check[j] == 0:
          check[j] = 1
          new = True
  if new == False:
    break

cnt = 0

for c in check:
  if c==1:
    cnt+=1
print(cnt-1)