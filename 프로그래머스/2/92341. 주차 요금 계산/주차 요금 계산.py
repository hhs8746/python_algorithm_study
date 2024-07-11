import math
def solution(fees, records):
    dt = fees[0] 
    dm = fees[1]
    et = fees[2]
    em = fees[3]
    d=dict()
    
    for i in range(len(records)):
        d[records[i].split(' ')[1]] =[]
    for i in range(len(records)):
        d[records[i].split(' ')[1]].append(list(map(int,records[i].split(' ')[0].split(':'))))
    for i in range(len(d)):
        if len(d[list(d.keys())[i]])%2 != 0:
            d[list(d.keys())[i]].append([23,59])
    

    all=[]
    ex=[]
    d2=dict()
    for k , v in d.items():
        
        am=0
        at=0
        for j in range(len(v)//2):
            
            if v[2*j+1][1] - v[2*j][1] >= 0:
                m=(v[2*j+1][1] - v[2*j][1])
                t=(v[2*j+1][0] - v[2*j][0])
            else:
                m=(v[2*j+1][1] - v[2*j][1]+60)
                t=(v[2*j+1][0] - v[2*j][0]-1)          
            at += t*60+m
        print(k,at)
        if at <= dt:
            ans = dm

        else:
            overt = at - dt
            overm = math.ceil(overt/et)*em
            ans = dm + overm
        am += ans
        d2[k]=am
        all.append(am)
    answer=[]    
    
        


    answer = []
    return list(dict(sorted(d2.items(), key=lambda x: x[0])).values())