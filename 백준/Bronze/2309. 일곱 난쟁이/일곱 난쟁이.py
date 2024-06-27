from itertools import combinations
l = []
for i in range(9):
    n = int(input())
    l.append(n)

all = list(combinations(l,7))
for j in all:
  if sum(j) == 100:
    jj = sorted(j)
    for nn in jj:
      print(nn)
    break