import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    
    nn=n
    all=[]
    num=[]
    cnt=0
    while True:
        cnt+=1
        f = n/k
        all.append(cnt)
        n=n/k
        if f<k:
            
            break
    for i in reversed(all):
        for j in reversed(range(k)):
    
            if (nn - k**i*j) >= 0:
                num.append(j)
                nn=nn - k**i*j
                break
    
    num.append(nn)
    alln = ""
    ans=[]
    ans2=[]
    num2 = ''.join(map(str, num))
    
    nums = num2.split('0')
    #nums= list(map(int,nums))
    
    for i in nums:
        if i != "":
            if is_prime(int(i)) == True:
                if i !="1":
                    ans.append(i)
            

                
            
        
    answer = -1
    return len(ans)