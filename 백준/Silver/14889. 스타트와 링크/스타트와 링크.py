import sys
from itertools import combinations
n = int(input())
m=[]
for i in range(n):
  m.append(list(map(int,input().split())))

min_diff=1e9

com = list(combinations([i for i in range(n)],int(n/2)))
for c in com:
  team_a = c
  team_b = []
  for i in range(n):
    if i not in team_a:
      team_b.append(i)
  sum1 = 0
  sum2 = 0

  for x in team_a:
    for y in team_a:
      sum1 += m[x][y]
  for x in team_b:
    for y in team_b:
      sum2 += m[x][y]

  diff = abs(sum1-sum2)

  if min_diff >= diff:
    min_diff = diff

print(min_diff)