def solution(today, terms, privacies):
    y, m, d = today.split('.')
    y =int(y)
    m=int(m)
    d=int(d)
    exam=dict()
   
    ans=[]
    yy=[]
    mm=[]
    dd=[]
    exaa=[]
    
    eee =[]
    for i in terms:
        exam[i.split(' ')[0]]=int(i.split(' ')[1])
        
    for j in privacies:
        yy.append(int(j.split('.')[0]))
        mm.append(int(j.split('.')[1]))
        dd.append(int(j.split('.')[2].split(' ')[0]))
        exaa.append(j.split('.')[2].split(' ')[1])
    
    for i in range(len(privacies)):
        if exam[exaa[i]] <=12:
            ee = [yy[i],mm[i]+exam[exaa[i]],dd[i]-1]
        else:
            ee = [yy[i]+exam[exaa[i]]//12,mm[i]+exam[exaa[i]]%12,dd[i]-1]
        
        if ee[2]<1:
            ee[1] = ee[1] - 1
            ee[2] = 28
            if ee[1]<1:
                ee[1] = 12
                ee[0] = ee[0]-1
            
        if ee[1]>12:
            ee[0] = ee[0]+1
            ee[1] = ee[1]-12
        eee.append(ee)
    for x in range(len(privacies)):
        if y > eee[x][0]:
            ans.append(x+1)
        elif y == eee[x][0] and m > eee[x][1]:
            ans.append(x+1)
        elif y == eee[x][0] and m == eee[x][1] and  d > eee[x][2]:
            ans.append(x+1)
        
        
    answer = ans
    return answer
