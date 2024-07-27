#백준 15666 N과 M(12)
from itertools import combinations_with_replacement

n,m = map(int,input().split(' '))

l=list(map(int,input().split()))
com = combinations_with_replacement(l, m)
answer = sorted(list(set(com)))
for i in range(len(answer)):
  answer[i]=tuple(sorted(answer[i]))
answer = list(sorted(set(answer)))
for i in answer:
  for j in range(len(i)):
    print(i[j],end=" ")
  print("")