from pickle import TRUE
# 백준 14916 거스름돈
n = int(input())
cnt=0
if n==3 or n==1:
  cnt=-1
else:
  while True:
    if (n-5)>3 or ((n-5)>=0 and (n-5)%2==0):
      n=n-5
      cnt+=1 
    else:
      cnt+=n//2
      break

print(cnt)