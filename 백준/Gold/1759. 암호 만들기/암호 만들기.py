from itertools import combinations
l,c = list(map(int,input().split()))
s = list(map(str,input().split()))
s.sort()
com = list(combinations(s,l))
cnt=0
ans=[]
answer=[]
for i in com:
  for w in i:
    if w in ['a','e','i','o','u']:
      cnt += 1
  cnt2 = l-cnt
  
  if cnt2 >=2 and cnt >=1:
    ans.append(''.join(i))
  cnt=0
 

for a in ans:
  print(a)