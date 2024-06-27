from collections import deque
import sys
m = int(input())
s=deque()
ss=deque()
for i in range(m):
    ss=list(map(str,sys.stdin.readline().split()))
    
    if len(ss)>1:
        ss[1] = int(ss[1])
    if ss[0] =='add' and ss[-1] not in s:
        s.append(ss[1])
    elif ss[0] == 'remove' and ss[-1] in s:
        s.remove(ss[1])
    elif ss[0] == 'check':
        if ss[1] in s:
            print(1)
        else:
            print(0)
    elif ss[0] == 'toggle':
        if ss[1] in s:
            s.remove(ss[1])
        else:
            s.append(ss[1])
    elif ss[0] == 'all':
        s = [num for num in range(1,21)]
    elif ss[0] == 'empty':
        s=deque()

