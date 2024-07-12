from itertools import product

def solution(n, info):
    c=[1]*len(info)
    ascore=[]
    b=[]
    ans=[]
    score=[0]*11
    for i in range(len(info)):
        if info[i] ==0:
            c[i] = 0
    
    all2=[]
    all = [i for i in range(n,-1,-1)]
    
    for i in range(len(info)):
        ascore.append((10-i)*c[i])
    
    for i in range(len(info)):
        all2.append([j for j in range(info[i]+1,-1,-1)])
    
    ll = list(product(*all2))
    
    
    lll=[]
    for i in ll:
        if sum(i)==n:
            lll.append(i)
    
    maxscore=0
    answe=[]
    che=0
    for i in range(len(lll)):
        
        ascore = [(10 - ss) * (info[ss] != 0) if info[ss] >= lll[i][ss] else 0 for ss in range(len(lll[i]))]
        tscore = [(10 - kk) * (lll[i][kk] != 0) if lll[i][kk] > info[kk] else 0 for kk in range(len(lll[i]))]
        if sum(tscore)>sum(ascore):
            che=1
            if maxscore<(sum(tscore)-sum(ascore)):
                maxscore=(sum(tscore)-sum(ascore))
                mscore = sum(tscore)
                answe=lll[i]
            elif maxscore == (sum(tscore)-sum(ascore)):
                if mscore<=sum(tscore):
                    answe=lll[i]
        if answe==[] or che==0:
            answe=[-1]
    
    return answe
    
    
        
    
