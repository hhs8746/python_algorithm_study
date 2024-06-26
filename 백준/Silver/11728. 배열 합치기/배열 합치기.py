import sys
n,m = map(int,input().split())

t1=list(map(int,sys.stdin.readline().split()))
t2=list(map(int,sys.stdin.readline().split()))

t3 = t1+t2
t3.sort()
print(' '.join(map(str, t3)))