K=int(input())
t=[]
for i in range(K):
    a=(int(input()))
    if a!=0:
        t.append(a)
    else:
        t.pop()
print(sum(t))