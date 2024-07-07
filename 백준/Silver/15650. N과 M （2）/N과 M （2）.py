# 백준 15650 N과 M(2)
from itertools import combinations
n,m = list(map(int,input().split()))
all = [i for i in range(1,n+1)]
com = list(combinations(all,m))

for j in com:
  print(*j)