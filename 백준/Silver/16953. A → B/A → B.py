# 백준 16953

n,m = map(int,input().split())

answer = 0
cnt=0
while n != m:
  if m%2 != 0 and len(str(m))>1 and str(m)[-1] == '1':
    m=int(str(m)[:-1])
    cnt+=1
  elif m%2 ==0:
    m = int(m/2)
    cnt+=1
  elif str(m)[-1] != '1' and m%2 == 1:
    cnt=-2
    break
  if m<n:
    cnt=-2
    break

print(cnt+1)
