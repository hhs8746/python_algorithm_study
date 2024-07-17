from itertools import product


def solution(friends, gifts):
    give = []
    get=[]
    products = list(product(friends,repeat=2))
    all=dict()
    all2=dict()
    givecount=dict()
    getcount = dict()
    cnt=0
    
    for i in friends:
        givecount[i]=0
        getcount[i]=0
    for i in products:
        if i[0] != i[1]:
            all[i[0]+' '+i[1]]=0
    
            
    
        
    for i in gifts:
        all2[i.split(' ')[0]]=0
        givecount[i.split(' ')[0]] += 1
        getcount[i.split(' ')[1]] += 1
        
    for i in gifts:
        if all[i]==0: 
            all[i] = 1
        else:
            all[i] += 1
        cnt+=1
    
    for k,v in list(all.items()):
        g1 = all[k]
        g2 = all[k.split(' ')[1]+' '+k.split(' ')[0]]
        point1 = givecount[k.split(' ')[0]] - getcount[k.split(' ')[0]]
        point2 = givecount[k.split(' ')[1]] - getcount[k.split(' ')[1]]
        try:
            if g1>g2:
                all2[k.split(' ')[0]] +=1
            elif g1<g2:
                all2[k.split(' ')[1]] +=1
            elif g1 == g2 and point1>point2:
                all2[k.split(' ')[0]] +=1
            elif g1 == g2 and point1<point2:
                all2[k.split(' ')[1]] +=1
            elif g1 == g2 and point1==point2:
                continue
        except:
            answer = 0
    try:
        answer = sorted(all2.values())[-1]/2
    except:
        answer = 0
    return answer

