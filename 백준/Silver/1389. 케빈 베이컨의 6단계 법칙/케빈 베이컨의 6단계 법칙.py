# 백준 1389 케빈 베이컨의 6단계 법칙
# 최단거리 구하기 문제!
# 각 노드에서 BFS 구하고 최단거리의 합의 최소값 찾기!

import sys
from collections import deque
n,m = list(map(int,input().split()))

adj = [[] for i in range(n)]

for i in range(m):
  a,b = list(map(int,input().split()))
  adj[a-1].append(b-1)
  adj[b-1].append(a-1)

ans=[]

for i in range(n):
  #모든 i를 시작으로 하는 BFS 시작
  visit = [0] * n
  
  dis = [-1] * n

  if visit[i] == 1:
    continue


  
  queue = deque([i])
  visit[i] = 1
  dis[i] = 0

  while len(queue) !=0:
      u = queue.popleft()
      for v in adj[u]:
        if visit[v] == 0:
          queue.append(v)
          visit[v]=1
          
          dis[v]=dis[u]+1
            
  kb = sum(dis)
  ans.append(kb)

for i in range(len(ans)):
  if ans[i] == min(ans):
    print(i+1)
    break