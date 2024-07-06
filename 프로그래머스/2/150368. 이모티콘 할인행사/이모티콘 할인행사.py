from itertools import product

def solution(users, emoticons):
    dis = [40,30,20,10]
    com =list(product(dis,repeat = len(emoticons)))
    money = []
    m=[]
    people = 0
    peoples=[0] * len(com)
    maxm = 0
    maxp=0
    mm=[0]* len(com)
    all=[]
    for i in range(len(users)):
        for ii,d in enumerate(com):
            for dd in range(len(d)):
                if d[dd] >= users[i][0]:
                    m.append(emoticons[dd]*(1-0.01*d[dd]))
            if sum(m) >= users[i][1]:
                money=0
                people += 1
                
            else:
                money=sum(m)
            
            m=[]
            peoples[ii] += people
            mm[ii] += money
            money=[]
            people=0
            money=0
            all.append([peoples[ii],mm[ii]])
    maxm=0
    for i in range(len(all)):
        if all[i][0] > maxp:
            maxp = all[i][0]
            maxm = all[i][1]
        elif all[i][0] == maxp and all[i][1] >= maxm: 
                maxm = all[i][1]
        # elif all[i][0] > maxp and all[i][1] == maxm: 
            
            
            
        
        
                
                
    answer = [maxp,maxm]
    return answer