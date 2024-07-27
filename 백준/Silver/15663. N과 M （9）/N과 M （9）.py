#백준 15663 N과 M(9)
from itertools import permutations

n,m = map(int,input().split(' '))

l=list(map(int,input().split()))
com = permutations(l, m)
answer = sorted(list(set(com)))
for i in answer:
  for j in range(len(i)):
    print(i[j],end=" ")
  print("")