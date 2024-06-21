all=[0]*43
answer=[]

for i in range(10):
    n= int(input())
    r = n%42
    all[r]=1

for j in range(0,42):
    if all[j]==1:
        answer.append(j)

print(len(answer))