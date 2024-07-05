#백준 2606 바이러스 
#DFS로 풀어보기

n = int(input())
m = int(input())
visit = [0]*n

adj = [[] for j in range(n)]
ans =[]
c = []
for i in range(m):
  a,b = list(map(int,input().split()))
  adj[a-1].append(b-1)
  adj[b-1].append(a-1)



def dfs(node):
  
  visit[node] = True
  for neighbor in adj[node]:
    if visit[neighbor] == False:
      dfs(neighbor)
      
  return sum(visit)-1

print(dfs(0))