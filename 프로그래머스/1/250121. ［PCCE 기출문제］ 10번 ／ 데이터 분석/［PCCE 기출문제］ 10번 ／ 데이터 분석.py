import pandas as pd
import numpy as np

def solution(data, ext, val_ext, sort_by):
    datas = dict()
    ans=[]
    datas['code'] = [] 
    datas['date'] = []
    datas['maximum'] = []
    datas['remain'] = []
    for i in data:
        datas['code'].append(i[0])
        datas['date'].append(i[1])
        datas['maximum'].append(i[2])
        datas['remain'].append(i[3])
        
#     for idx,i in enumerate(data[ext]):
#         if i <= val_ext:
#             ans.append(idx)
        
    
    df = pd.DataFrame({
    'code': [],
    'date': [],
    'maximum': [],
    'remain': []
    })
    df['code'] = [i for i in datas['code']]
    df['date'] = [i for i in datas['date']]
    df['maximum'] = [i for i in datas['maximum']]
    df['remain'] = [i for i in datas['remain']]
    df = df[df[ext] <= val_ext]
    
    df.sort_values(by=sort_by,inplace=True)
    
    for row in df.values:
        ans.append(list(row))
    for i in ans:
        for j in range(len(i)):
            i[j] = int(i[j])
    
    return ans