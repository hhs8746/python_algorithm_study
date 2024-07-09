def solution(id_list, report, k):
    p = dict()
    pn=dict()
    ex=dict()
    cn=[]
    st=[]
    for i in id_list:
        p[i] = []
        pn[i] = []
        ex[i] = []
        
    for i in range(len(report)):
        p[report[i].split(' ')[0]].append(report[i].split(' ')[1])
        p[report[i].split(' ')[0]]=list(set(p[report[i].split(' ')[0]]))
        
        
    for n1, n2 in list(p.items()):
        for pp in n2:
            
            pn[pp].append(1)
            ex[pp] = [sum(pn[pp])]
    for kk, v in list(ex.items()):
        try:
            if v[0]>=k:
                st.append(kk)
        except:
            continue
    for sss in id_list:
        cnt=0
        for ss in st:
            if ss in p[sss]:
                cnt +=1
        cn.append(cnt)
                
    
    answer = []
    return cn