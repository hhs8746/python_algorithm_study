def solution(survey, choices):
    answer=""
    all=[]
    ans = dict()
    s=["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]
    alls = ["R","T","C","F","J","M","A","N"]
    for i in range(8):
        all.append(s[i][0])
        all.append(s[i][1])
    all = list(set(all))
    for i in all:
        ans[i]=0
    for i in range(len(survey)):
        if choices[i]>4:
            ans[survey[i][1]]+=choices[i]-4
        else:
            ans[survey[i][0]]+=4-choices[i]
    ans2 = list(reversed(sorted(ans.items(),key=lambda x: x[1])))
    ans3=[]
    cnt=0
    # for i in ans2:
    #     if (i[0] =="R" or i[0] =="T"):
    #         ans3.append(i)
    #         answer+=i[0]
    for j,i in enumerate(alls):
        cnt+=1
        if cnt%2==1:
            score1 = ans[alls[j]]
            score2 = ans[alls[j+1]]
            if score1 > score2:
                answer+=alls[j]
            elif score1 < score2:
                answer+=alls[j+1]
            else:
                if ord(alls[j])>ord(alls[j+1]):
                    answer+= alls[j+1]
                else:
                    answer+=alls[j]
    return answer