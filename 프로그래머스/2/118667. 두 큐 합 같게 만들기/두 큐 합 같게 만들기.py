from collections import deque




def solution(queue1, queue2):
    queue01 = deque(queue1).copy()
    queue02 = deque(queue2).copy()
    queue1 =deque(queue1)
    queue2 = deque(queue2)
    target = (sum(queue1)+sum(queue2))/2
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    cnt=0
    
    if sum1 == sum2:
        cnt = 0
        return 0
            
    elif (sum1 + sum2) % 2 == 1:
        cnt = -1
        return -1
            
    while True:
        
        if sum1>target:
            l = queue1.popleft()
            queue2.append(l)
            
            cnt+=1
            sum1 -= l
            sum2 += l
            
        elif sum2>target:
            l = queue2.popleft()
            queue1.append(l)
            
            cnt+=1
            sum1 += l
            sum2 -= l
        else:
            break
            
        if cnt==3*len(queue01):
            cnt=-1
            break
            
        
    
    return cnt