s = input()
def strint(a):
    n= ord(a) - ord('a')
    return int(n)
answer=[]

all=[-1]*26
for j,i in enumerate(s):
    if all[strint(i)] == -1:
        all[strint(i)]=j

    

print(*all)