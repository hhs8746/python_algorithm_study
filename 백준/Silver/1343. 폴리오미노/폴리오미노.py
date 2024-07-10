#백준 1343 폴리노미노
s=input()
ss = s.split('.')
ans=[]
ans2=0
if '.' in s:
  for i in ss:
    n=0
    m=0
    if i != '': 
      if len(i)%2 !=0:
        ans2=-1
        break
      else:
        n += len(i)//4
        m += (len(i)-n*4)//2
        ans.append(n*"AAAA"+m*"BB")
      ans.append('.')
    else:
      ans.append('.')
else:
  for i in ss:
    n=0
    m=0
    if i != '': 
      if len(i)%2 !=0:
        ans2=-1
        break
      else:
        n += len(i)//4
        m += (len(i)-n*4)//2
        ans.append(n*"AAAA"+m*"BB")
      ans.append('.')
    else:
      ans.append('.')
    
    
if ans2 !=0:
  print(-1)
else:
  if ss[-1] != '.':
    print(''.join(ans)[0:-1])
  else:
    print(''.join(ans)[0:-1]+s.split('X')[-1])