# 백준 11399 ATM
n = int(input())
p = list(map(int,input().split()))
p.sort()
cnt=0
all=0
for i in p:
  cnt += i
  all += cnt
print(all)