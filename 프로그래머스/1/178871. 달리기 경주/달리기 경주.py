def solution(players, callings):
    d = dict()
    for i,j in enumerate(players):
        d[j] = i+1
    nd=dict()
    for k,v in d.items():
        nd[v]=k
    
    for i in range(len(callings)):
        val = d[callings[i]]
        d[nd[val-1]]+=1
        d[callings[i]] -= 1
        
        nd[val] = nd[val-1]
        
        nd[val-1]=callings[i]
        
            
    answer = []
    return sorted(d,key=lambda x: d[x])