all=[0]*31

for i in range(28):
    n = int(input())
    all[n] = 1

answer = []
for j in range(1,31):
    if all[j] == 0:
        print(j)