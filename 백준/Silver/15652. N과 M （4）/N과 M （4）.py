#백준 15652 N과 M(4)
from itertools import combinations_with_replacement

n,m = map(int,input().split(' '))
all = [i for i in range(1,n+1)]
com = combinations_with_replacement(all, m)
answer = list(com)
for i in answer:
  for j in range(len(i)):
    print(i[j],end=" ")
  print("")