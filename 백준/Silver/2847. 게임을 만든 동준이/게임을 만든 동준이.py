# 백준 2847 게임을 만든 동준이
n = int(input())
s=[]
cnt = 0
for i in range(n):
  s.append(int(input()))
for j in reversed(range(1,len(s))):
  if s[j] <= s[j-1]:
    cnt += 1 + s[j-1] - s[j]
    s[j-1] = s[j]-1
print(cnt)