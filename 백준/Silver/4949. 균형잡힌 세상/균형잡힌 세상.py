while True:
  s = input()
  stack=[]
  answer='yes'
  if s == '.':
    break
  for c in s:
    if c=='(' or c=='[':
      stack.append(c)
    if c==')':
      if len(stack)==0:
        answer='no'
        break

      if len(stack) !=0 and (stack[-1]=='('):
        stack.pop()
      else:
        answer='no'
        break   

    elif c==']':
      if len(stack)==0:
        answer='no'
        break

      if len(stack) !=0 and (stack[-1]=='['):
        stack.pop()
      else:
        answer='no'
        break 

  if len(stack)!=0:
    answer='no'
  print(answer)