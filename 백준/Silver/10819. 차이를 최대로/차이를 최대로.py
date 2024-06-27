import sys
from itertools import permutations
n = int(input())
l = list(map(int,sys.stdin.readline().split()))
lp = list(permutations(l,n))
sum1 = 0

max0=0
for i in lp:
    sum1 = 0
    for j in range(len(l)-1):
        sum1 = sum1+ abs(i[j]-i[j+1])
        if max0 <= sum1:
            max0 = sum1
print(max0)
        