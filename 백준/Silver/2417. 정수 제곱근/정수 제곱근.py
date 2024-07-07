#백준 2417 정수 제곱근
import math
n= int(input())
if math.ceil(math.sqrt(n)) * math.ceil(math.sqrt(n)) >= n:
  print(math.ceil(math.sqrt(n)))
else:
  print(math.ceil(math.sqrt(n))+1)