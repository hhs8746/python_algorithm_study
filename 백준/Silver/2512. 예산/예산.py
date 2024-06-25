import sys

n = int(input())
b=[]

b=list(map(int,input().split()))
m = int(input())
left = 0
right = max(b)
x=[]
cnt2=0
for nn in b:
  cnt2 += nn
if cnt2 <= m:
  print(max(b))
else:
  while left <= right-1:
    mid = (left + right) //2
    sum=0
    for i in range(n):
      sum += min(mid, b[i])
    if sum >m:
      right=mid
      x.append(mid)

    elif sum <= m:
      left = mid
      x.append(mid)
    if len(x) >1 and mid == x[-2]:
      
      print(mid)
      break
