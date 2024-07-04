import sys
from collections import deque
input = sys.stdin.readline
n,m = list(map(int,input().split()))
adj = [[] for j in range(n)]
for i in range(m):
  u,v = list(map(int,input().split()))
  adj[u-1].append(v-1)
  adj[v-1].append(u-1)

visit = [False] *n
count = 0

for i in range(n):
  if visit[i]:
    continue
  
  # BFS 시작
  count += 1

  queue = deque([i])
  visit[i] = True

  while len(queue) != 0:
    u = queue.popleft()

    for v in adj[u]:
      if not visit[v]:
        queue.append(v)
        visit[v] = True
print(count)