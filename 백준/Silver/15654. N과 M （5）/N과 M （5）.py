#백준 15654 N과 M(5)
from itertools import permutations

n,m = map(int,input().split(' '))

l=list(map(int,input().split()))
l.sort()

com = permutations(l, m)
answer = list(com)
for i in answer:
  for j in range(len(i)):
    print(i[j],end=" ")
  print("")
